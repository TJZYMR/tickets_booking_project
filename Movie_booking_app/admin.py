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
    SeatState,
    ShowWiseSeats,
)
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(
    [
        SeatState,
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
        ShowWiseSeats,
    ]
)


@admin.register(Booking)
class BookingAdmin(ImportExportModelAdmin):
    pass
