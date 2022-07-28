from django.contrib import admin

from Movie_booking_app.models.payments import Coupen
from .models import (
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

# Register your models here.
admin.site.register(
    [
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
    ]
)
