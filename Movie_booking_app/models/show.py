from django.db import models
from Movie_booking_app.models.cinema import Cinema
from Movie_booking_app.models.cinemahall import CinemaHall
from Movie_booking_app.models.movie import Movie


# 1.a movie can have multiple shows=>done
# 2.a cinemahall can have one movie at a time.=>done
# 3.one cinema can have manyshows.=>done
class Show(models.Model):
    created_on = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True)
    cinema_hall = models.OneToOneField(CinemaHall, on_delete=models.CASCADE, null=True)
