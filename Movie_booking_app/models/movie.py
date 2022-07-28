from django.db import models

from Movie_booking_app.models.util import Timestamp

# 1.a movie can have multiple shows.=>done
# 2.a movie can have multiple cinemas.=>done
class Movie(Timestamp):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    year = models.IntegerField()
    duration = models.IntegerField()
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()
    language = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.title
