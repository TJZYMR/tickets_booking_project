import email
from turtle import st
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
    NotificationType,  #
)
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
)
from rest_framework import status
import logging

logger = logging.getLogger(__name__)
# class BookingViewSet(viewsets.ModelViewSet):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer


# class SeatTypeViewSet(viewsets.ModelViewSet):
#     queryset = SeatType.objects.all()
#     serializer_class = SeatTypeSerializer


# class CinemaViewSet(viewsets.ModelViewSet):
#     queryset = Cinema.objects.all()
#     serializer_class = CinemaSerializer


# class CinemaHallViewSet(viewsets.ModelViewSet):
#     queryset = CinemaHall.objects.all()
#     serializer_class = CinemaHallSerializer


# class CinemaHallSeatViewSet(viewsets.ModelViewSet):
#     queryset = CinemaHallSeat.objects.all()
#     serializer_class = CinemaHallSeatSerializer


# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


# class ShowViewSet(viewsets.ModelViewSet):
#     queryset = Show.objects.all()
#     serializer_class = ShowSerializer


# class PaymentStatusViewSet(viewsets.ModelViewSet):
#     queryset = PaymentStatus.objects.all()
#     serializer_class = PaymentStatusSerializer


# class BookingStatusViewSet(viewsets.ModelViewSet):
#     queryset = BookingStatus.objects.all()
#     serializer_class = BookingStatusSerializer


# class AccountStatusViewSet(viewsets.ModelViewSet):
#     queryset = AccountStatus.objects.all()
#     serializer_class = AccountStatusSerializer


class UserViewSet(viewsets.ViewSet):
    """User Registration API"""

    def create(self, request):
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
        try:
            user = User.objects.get(slug=slug)
            serializer = UserSerializer(user)
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
