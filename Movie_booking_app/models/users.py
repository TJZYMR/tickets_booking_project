from django.db import models
from django.contrib.auth.models import AbstractUser

from Movie_booking_app.models.statuses import AccountStatus
from autoslug import AutoSlugField

USER_CHOICES = (
    ("Customer", "CUSTOMER"),
    ("Admin", "ADMIN"),
    ("Fronenddesk", "FRONTENDDESK"),
)


class User(AbstractUser):
    user_type = models.CharField(
        max_length=250, choices=USER_CHOICES, default="customer"
    )
    account_status = models.ForeignKey(
        AccountStatus,
        on_delete=models.CASCADE,
        default=0,
        null=True,  # , editable=False
    )
    slug = AutoSlugField(
        populate_from="username",
        default="",
        unique=True,
        editable=True,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        app_label = "Movie_booking_app"
