from django_extensions.db.fields import AutoSlugField
from django.db import models

from Movie_booking_app.models.util import Timestamp


class SeatType(models.Model):  # regular, premium, vip, vip_premium
    seat_type = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from=["seat_type"], unique=True, editable=True)

    def slugify_function(self, content):
        return content.replace(" ", "-").lower()

    def __str__(self):
        return self.seat_type

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
    # show = models.ForeignKey(Show, on_delete=models.CASCADE, null=True)
    slug = AutoSlugField(populate_from=["name"], unique=True, editable=True)
    # cinema_hall
    def slugify_function(self, content):
        return content.replace(" ", "-").lower()

    def __str__(self):
        return self.name

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=["show", "name"], name="unique show and name"
    #         )
    #     ]
