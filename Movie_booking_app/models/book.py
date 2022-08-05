# import datetime
# from io import open_code
# from tkinter import E
from django.db import models as mod
from Movie_booking_app.models.cinemahall import CinemaHall
from Movie_booking_app.models.cinemahallseat import CinemaHallSeat

from Movie_booking_app.models.movie import Movie
from Movie_booking_app.models.payments import PaymentMode
from Movie_booking_app.models.statuses import BookingStatus, PaymentStatus
from Movie_booking_app.models.users import User
from Movie_booking_app.models.show import Show
from Movie_booking_app.models.cinema import Cinema
from django_extensions.db.fields import AutoSlugField

# 1.a booking can have many users.=>done
# 2.a booking can have one user.=>done
# 3.a booking can have one booking status.=>done
# 4.a booking can have one payment status.=>done
# 5.a booking can have one movie.=>done
# 6.a booking can have one cinema.=>done
# 7.a booking can have one cinema hall.=>done
# 8.a booking can have one show.=>done
class Booking(mod.Model):
    movie = mod.ForeignKey(Movie, on_delete=mod.CASCADE)
    cinema = mod.ForeignKey(Cinema, on_delete=mod.CASCADE)
    cinemahall = mod.ForeignKey(CinemaHall, on_delete=mod.CASCADE, null=True)
    show = mod.ForeignKey(Show, on_delete=mod.CASCADE, null=True)
    payment_status = mod.ForeignKey(
        PaymentStatus, on_delete=mod.CASCADE, null=True, default=2
    )
    booking_status = mod.ForeignKey(
        BookingStatus, on_delete=mod.CASCADE, null=True, default=1
    )
    booking_date_time = mod.DateTimeField(auto_now_add=True, blank=True, null=True)
    seats = mod.ManyToManyField(CinemaHallSeat, blank=True)
    total_amount = mod.IntegerField()
    payment_mode = mod.ForeignKey(PaymentMode, on_delete=mod.CASCADE, null=True)
    user = mod.ForeignKey(User, on_delete=mod.CASCADE, null=True)
    slug = AutoSlugField(
        populate_from=["user__username"], unique=True, editable=True, default=""
    )

    def slugify_function(self, content):
        return (
            content.replace(" ", "-").lower()
            + "-"
            + str(self.show.date)
            + "-"
            + str(self.show.start_time)
            + "-"
            + str(self.cinema.name)
            + "-"
            + str(self.cinemahall.name)
        )

    def __str__(self):
        return self.slug
