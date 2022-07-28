from django.db import models
from Movie_booking_app.models.cinemahall import CinemaHall
from Movie_booking_app.models.movie import Movie

from Movie_booking_app.models.util import Timestamp


class SeatType(models.Model):  # regular, premium, vip, vip_premium
    seat_type = models.CharField(max_length=100)

    def __str__(self):
        return self.booking_status

    class Meta:
        verbose_name_plural = "Seat-Type"


# 1.one cinema can have multiple movies and one movie can be in many cinemas.(manytomany field)=>done
# 2.one cinema can have multiple cinemahalls(onetomany field)=>done
# 3.a show can be in multiple cinemas=>done
class Cinema(Timestamp):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, null=True)
    movie = models.ManyToManyField(Movie, blank=True, null=True)

    def __str__(self):
        return self.name
