from django.db import models as mod
from Movie_booking_app.models.cinemahall import CinemaHall

from Movie_booking_app.models.movie import Movie
from Movie_booking_app.models.statuses import BookingStatus, PaymentStatus
from Movie_booking_app.models.users import User
from Movie_booking_app.models.show import Show
from Movie_booking_app.models.cinema import Cinema

# 1.a booking can have many users.=>done
# 2.a booking can have one user.=>done
# 3.a booking can have one booking status.=>done
# 4.a booking can have one payment status.=>done
# 5.a booking can have one movie.=>done
# 6.a booking can have one cinema.=>done
# 7.a booking can have one cinema hall.=>done
# 8.a booking can have one show.=>done
class Booking(mod.Model):
    movie = mod.OneToOneField(Movie, on_delete=mod.CASCADE)
    cinema = mod.OneToOneField(Cinema, on_delete=mod.CASCADE)
    cinemahall = mod.OneToOneField(CinemaHall, on_delete=mod.CASCADE, null=True)
    show = mod.OneToOneField(Show, on_delete=mod.CASCADE, null=True)
    payment_status = mod.OneToOneField(PaymentStatus, on_delete=mod.CASCADE, null=True)
    booking_status = mod.OneToOneField(BookingStatus, on_delete=mod.CASCADE, null=True)
    booking_date_time = mod.DateTimeField(auto_now_add=True, blank=True, null=True)
    seats = mod.CharField(max_length=100)
    total_amount = mod.IntegerField()
    user = mod.ForeignKey(User, on_delete=mod.CASCADE, null=True)

    def __str__(self):
        return self.movie.title
