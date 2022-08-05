# from re import M
from django.db import models
from Movie_booking_app.models.movie import Movie


class NotificationType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Notification(models.Model):
    """
    Notification model
    """

    notification_type = models.OneToOneField(NotificationType, on_delete=models.CASCADE)
    notification_message = models.TextField(max_length=1000)
    notification_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_type

    class Meta:
        verbose_name_plural = "Notifications"
