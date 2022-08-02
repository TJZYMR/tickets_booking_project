from rest_framework import serializers

from Movie_booking_app.models import (
    Booking,
    SeatType,
    Cinema,
    CinemaHall,
    CinemaHallSeat,
    Movie,
    Show,
    PaymentStatus,
    BookingStatus,
    AccountStatus,
    User,
    PaymentMode,
    Payment,
    Coupen,
    Notification,
    NotificationType,
)


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class SeatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatType
        fields = "__all__"


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"


class CinemaHallSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHallSeat
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "title",
            "description",
            "year",
            "genre",
            "rating",
            "language",
            "country",
        ]


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = "__all__"


class PaymentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentStatus
        fields = "__all__"


class BookingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingStatus
        fields = "__all__"


class AccountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountStatus
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class PaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMode
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class CoupenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupen
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationType
        fields = "__all__"
