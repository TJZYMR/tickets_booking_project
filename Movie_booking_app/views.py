from datetime import date
import email
import re
from rest_framework.response import Response
from rest_framework import viewsets
from Movie_booking_app import serializers
from Movie_booking_app.models import (
    Booking,  #
    SeatType,  #
    Cinema,  #
    CinemaHall,  #
    CinemaHallSeat,  #
    Movie,  #
    Show,  #
    PaymentStatus,  #
    BookingStatus,  #
    AccountStatus,  #
    User,  #
    PaymentMode,  #
    Payment,  #
    Coupen,  #
    Notification,  #
    NotificationType,
    cinema,
    movie,  #
)
from Movie_booking_app.models.statuses import SeatState
from Movie_booking_app.serializers import (
    BookingSerializer,
    SeatTypeSerializer,
    CinemaSerializer,
    CinemaHallSerializer,
    CinemaHallSeatSerializer,
    MovieSerializer,
    ShowSerializer,
    PaymentStatusSerializer,
    BookingStatusSerializer,
    AccountStatusSerializer,
    UserSerializer,
    PaymentModeSerializer,
    PaymentSerializer,
    CoupenSerializer,
    NotificationSerializer,
    NotificationTypeSerializer,
    UserProfileSerializer,
    ShowMovieSerializer,
)
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework import status
import logging

from Movie_booking_app.tasks import seat_timeout, add

logger = logging.getLogger(__name__)
# class BookingViewSet(viewsets.ModelViewSet):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer


# class SeatTypeViewSet(viewsets.ModelViewSet):
#     queryset = SeatType.objects.all()
#     serializer_class = SeatTypeSerializer

from django.db.models import Prefetch

# from django.db.models import Prefetch

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie


class ShowViewSet(viewsets.ModelViewSet):
    def retrieve(self, request, **kwargs):
        try:
            # for getting query parameters' value we added kwargs and below request to get method
            slug = request.GET.get("cinema")
            queryset = Show.objects.all().filter(cinema__slug=slug)
            serializer = ShowSerializer(queryset, many=True)
            if serializer.data:
                logger.info("'Cinema exist'")
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                raise Exception("Cinema does not exist")
        except Exception as e:
            logger.error(f"'{e}'")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CinemaViewSet(viewsets.ModelViewSet):
    def retrieve(self, request, **kwargs):
        try:
            movie = request.GET.get("movie")
            location = request.GET.get("location")
            queryset = Show.objects.all().filter(
                movie__slug=movie, cinema__city=location, date=date.today()
            )
            serializer = ShowMovieSerializer(queryset, many=True)
            if serializer.data:
                logger.info("'Movie exist'")
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                raise Exception("Movie does not exist")
        except Exception as e:
            logger.error(f"'{e}'")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# class CinemaHallViewSet(viewsets.ModelViewSet):
#     queryset = CinemaHall.objects.all()
#     serializer_class = CinemaHallSerializer


# class CinemaHallSeatViewSet(viewsets.ModelViewSet):
#     queryset = CinemaHallSeat.objects.all()
#     serializer_class = CinemaHallSeatSerializer


class MovieViewSet(viewsets.ViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        "slug",
        "year",
        "genre",
        "rating",
        "language",
    )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        logger.debug(
            "'filtering queryset on the basis of the query param is being fetched'"
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# class ShowViewSet(viewsets.ModelViewSet):
#     queryset = Show.objects.all()
#     serializer_class = ShowSerializer


# class PaymentStatusViewSet(viewsets.ModelViewSet):
#     queryset = PaymentStatus.objects.all()
#     serializer_class = PaymentStatusSerializer

from django.db import transaction

from django.core.signals import request_finished

# def timeout(seats, booking_id):

#     print("singal started calling")
#     import time

#     payment_pending = PaymentStatus.objects.get(id=2)
#     book_cancelled = BookingStatus.objects.get(id=5)
#     payment_cancelled = PaymentStatus.objects.get(id=4)
#     print(seats, booking_id)
#     time.sleep(5)
#     if Booking.objects.get(id=booking_id).payment_status == payment_pending:
#         Booking.objects.filter(id=booking_id).update(
#             payment_status=payment_cancelled, booking_status=book_cancelled
#         )
#         for seat in CinemaHallSeat.objects.filter(id__in=seats):
#             seat.state = SeatState.objects.get(id=1)
#             seat.save()
#     print("signal finished!")


# now try to call celery task after seat booked,so no more waiitng time for lient s after booking.


class BookViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            # for getting query parameters' value we added kwargs and below request to get method
            # user_id = request.data.get("user_id")
            movie_id = request.data["movie_id"]
            cinema_id = request.data["cinema_id"]
            cinemahall_id = request.data["cinemahall_id"]
            show_id = request.data["show_id"]
            # payment_status = request.data["payment_status"]
            # booking_status = request.data["booking_status"]
            seats = request.data["seats"]
            total_amount = request.data["total_amount"]
            user_id = request.data["user_id"]
            payment_mode = request.data.get("payment_mode")
            # coupen_id = request.data.get("coupen_id")
            payment_mode = PaymentMode.objects.get(id=payment_mode)
            logger.info("'Started the booking process'")
            with transaction.atomic():
                for seat in CinemaHallSeat.objects.filter(id__in=seats):
                    if seat.state == SeatState.objects.get(id=6):
                        raise Exception("Seat is already booked")
                    else:
                        seat.state = SeatState.objects.get(id=6)
                        seat.save()
                queryset = Booking.objects.create(
                    user_id=user_id,
                    movie_id=movie_id,
                    cinema_id=cinema_id,
                    cinemahall_id=cinemahall_id,
                    show_id=show_id,
                    # seats=seats,
                    total_amount=total_amount,
                    payment_mode=payment_mode,
                )
                # , {"seats": seats, "booking_id": queryset.id}
                # request_finished.connect(my_callback, )
                seat_timeout.apply_async((seats, queryset.id), countdown=25)
                # add.delay(1, 2)
                queryset.seats.set(seats)
                serializer = BookingSerializer(queryset)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            # else:
            #     raise Exception("All fields are not present")
        except Exception as e:
            logger.error(f"'{e}'")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# class AccountStatusViewSet(viewsets.ModelViewSet):
#     queryset = AccountStatus.objects.all()
#     serializer_class = AccountStatusSerializer


class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        """User Registration API"""
        serializer = UserSerializer(data=request.data)
        if User.objects.filter(
            username=request.data["username"],
        ).exists():
            logger.debug("'Username already exists'")
            return Response(
                {"message": "Username already exists"}, status=status.HTTP_409_CONFLICT
            )
        if User.objects.filter(
            first_name=request.data["username"],
            email=request.data["email"],
        ).exists():
            logger.debug("'User already exists'")
            return Response(
                {"message": "User already exists"}, status=status.HTTP_409_CONFLICT
            )

        if serializer.is_valid():
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.save()

        logger.info(
            "'User created successfully for user "
            + str(request.data["first_name"])
            + "-"
            + str(request.data["last_name"])
            + "'"
        )
        return Response(
            # serializer.data,#bcs we don't want to send all data in the response to the client back,so commented this out.
            {
                "message": "User created successfully for user "
                + str(request.data["first_name"])
                + "-"
                + str(request.data["last_name"])
            },
            status=status.HTTP_201_CREATED,
        )

    def retrieve(self, request, slug):
        """User Profile GET request API"""
        try:
            user = User.objects.get(slug=slug)
            serializer = UserProfileSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(
                {"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND
            )


# class PaymentModeViewSet(viewsets.ModelViewSet):
#     queryset = PaymentMode.objects.all()
#     serializer_class = PaymentModeSerializer


# class PaymentViewSet(viewsets.ModelViewSet):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer


# class CoupenViewSet(viewsets.ModelViewSet):
#     queryset = Coupen.objects.all()
#     serializer_class = CoupenSerializer


# class NotificationViewSet(viewsets.ModelViewSet):
#     queryset = Notification.objects.all()
#     serializer_class = NotificationSerializer


# class NotificationTypeViewSet(viewsets.ModelViewSet):
#     queryset = NotificationType.objects.all()
#     serializer_class = NotificationTypeSerializer
