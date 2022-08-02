from django_extensions.db.fields import AutoSlugField
from django.db import models
from Movie_booking_app.models.cinema import Cinema
from Movie_booking_app.models.util import Timestamp

# 1.a cinema can have multiple CinemaHalls.=>done
# 2.one cinemahall can run one movie at one time.=>done
# 3.one cinemahall can have multiple shows and a show can be in many cinemahall(manytomany).=>done
class CinemaHall(Timestamp):
    name = models.CharField(max_length=100)
    # movie = models.OneToOneField(Movie, on_delete=models.CASCADE, null=True)
    total_seats = models.IntegerField()
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True)
    slug = AutoSlugField(populate_from=["name"], unique=True, editable=True)

    def slugify_function(self, content):
        return content.replace(" ", "-").lower()

    def __str__(self):
        return self.name
