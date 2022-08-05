from django.core.management.base import BaseCommand
from django.utils import timezone
from Movie_booking_app.models.show import Show


class Command(BaseCommand):
    help = "Deletes expired rows in the Shows Table"

    def handle(self, *args, **options):
        now = timezone.now()
        Show.objects.filter(date__lt=now).delete()
