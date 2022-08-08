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

from Movie_tickets_booking.settings import EMAIL_HOST_USER
from Movie_tickets_booking.celery import app

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
        PaymentStatus, on_delete=mod.CASCADE, null=True, default=3
    )
    booking_status = mod.ForeignKey(
        BookingStatus, on_delete=mod.CASCADE, null=True, default=2
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

    #! this signal is for detecting changes and sending the signal with the actions that we want to do.
    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_instance = Booking.objects.get(pk=self.pk)
            if old_instance.payment_status != self.payment_status:
                if self.payment_status == PaymentStatus.objects.get(id=1):
                    #!we are not directly calling by delay but just sending task in the queue to be executed.
                    app.send_task(
                        "send_mail_to",
                        (
                            self.id,
                            self.user.email,
                            self.payment_status.id,
                            {
                                "user": self.user.username,
                                "movie": self.movie.slug,
                                "cinema": self.cinema.name,
                                "cinemahall": self.cinemahall.name,
                                "show": self.show.date,
                                "show_time": self.show.start_time,
                                # "seats": self.seats.all(),
                            },
                        ),
                    )
                    print("payment done and your booking is confirmed")
                    self.booking_status = BookingStatus.objects.get(id=4)
                elif self.payment_status == PaymentStatus.objects.get(id=2):
                    print("payment is being cancelled")
                    app.send_task(
                        "send_mail_to",
                        (self.id, self.user.email, self.payment_status.id),
                    )
                    self.booking_status = BookingStatus.objects.get(id=3)

        super().save(*args, **kwargs)
