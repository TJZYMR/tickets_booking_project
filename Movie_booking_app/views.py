from datetime import date
from rest_framework.response import Response
from rest_framework import viewsets
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
from django_filters import rest_framework as filters
from rest_framework import status
import logging

from Movie_booking_app.tasks import seat_timeout


logger = logging.getLogger(__name__)
# class BookingViewSet(viewsets.ModelViewSet):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer


# class SeatTypeViewSet(viewsets.ModelViewSet):
#     queryset = SeatType.objects.all()
#     serializer_class = SeatTypeSerializer

from django.db.models import Prefetch


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


from django.db import transaction


class BookViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            # !for getting query parameters' value we added kwargs and below request to get method
            movie_id = request.data["movie_id"]
            cinema_id = request.data["cinema_id"]
            cinemahall_id = request.data["cinemahall_id"]
            show_id = request.data["show_id"]
            seats = request.data["seats"]
            total_amount = request.data["total_amount"]
            user_id = request.data["user_id"]
            payment_mode = request.data["payment_mode"]
            payment_mode = PaymentMode.objects.get(id=payment_mode)
            logger.info("'Started the booking process'")
            with transaction.atomic():
                if Show.objects.get(id=show_id).is_active is False:
                    raise Exception("Show is not active")
                for seat in CinemaHallSeat.objects.filter(id__in=seats):
                    if seat.state == SeatState.objects.get(id=2):
                        raise Exception("Seat is already booked")
                    else:
                        seat.state = SeatState.objects.get(id=2)
                        seat.save()
                queryset = Booking.objects.create(
                    user_id=user_id,
                    movie_id=movie_id,
                    cinema_id=cinema_id,
                    cinemahall_id=cinemahall_id,
                    show_id=show_id,
                    total_amount=total_amount,
                    payment_mode=payment_mode,
                )
                seat_timeout.apply_async((seats, queryset.id), countdown=20)
                # ! setting the seats many to many field here,like this,it is set like this in this relationship.
                queryset.seats.set(seats)
                serializer = BookingSerializer(queryset)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"'{e}'")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


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
