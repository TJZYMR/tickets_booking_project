from django_extensions.db.fields import AutoSlugField
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
    rating = models.FloatField(default=0)
    language = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=["title"], unique=True, editable=True)

    def slugify_function(self, content):
        return content.replace(" ", "-").lower()

    def __str__(self):
        return self.title
