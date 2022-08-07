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
        fields = [
            "total_amount",
            "movie",
            "cinema",
            "cinemahall",
            "show",
            "booking_status",
            "seats",
            "payment_status",
        ]


class SeatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatType
        fields = "__all__"


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ["name", "state", "city", "country", "phone", "email"]


class CinemaHallSerializer(serializers.ModelSerializer):
    # for selecting only one field from the other serializers

    cinemaname = serializers.SlugRelatedField(
        source="cinema", slug_field="name", read_only=True
    )

    class Meta:
        model = CinemaHall
        fields = ["name", "total_seats", "cinemaname", "available_seats"]


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
    movie = MovieSerializer()
    cinema = CinemaSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = Show
        fields = [
            "start_time",
            "end_time",
            "date",
            "movie",
            "cinema",
            "cinema_hall",
        ]


class ShowMovieSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer()

    class Meta:
        model = Show
        fields = [
            "start_time",
            "cinema",
        ]


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
