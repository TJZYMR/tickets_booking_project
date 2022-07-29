from autoslug import AutoSlugField
from django.db import models
from Movie_booking_app.models.movie import Movie
from Movie_booking_app.models.util import Timestamp

# 1.a cinema can have multiple CinemaHalls.=>done
# 2.one cinemahall can run one movie at one time.=>done
# 3.one cinemahall can have multiple shows and a show can be in many cinemahall(manytomany).=>done
class CinemaHall(Timestamp):
    name = models.CharField(max_length=100)
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, null=True)
    total_seats = models.IntegerField()
    slug = AutoSlugField(
        populate_from="name",
        default="",
        unique=True,
        editable=True,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
