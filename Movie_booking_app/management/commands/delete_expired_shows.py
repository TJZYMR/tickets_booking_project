from django.core.management.base import BaseCommand
from django.utils import timezone
from Movie_booking_app.models.cinemahallseat import CinemaHallSeat
from Movie_booking_app.models.show import Show
from Movie_booking_app.models.statuses import SeatState


class Command(BaseCommand):
    help = "Deletes expired rows in the Shows Table"

    def handle(self, *args, **options):
        now = timezone.now()
        expired_shows = Show.objects.filter(date__lt=now)
        if expired_shows:
            for show in expired_shows:
                show.is_active = False
                show.save()
                for seat in CinemaHallSeat.objects.filter(
                    cinema_hall_id=show.cinema_hall_id
                ):
                    seat.state = SeatState.objects.get(id=1)
                    seat.save()

        self.stdout.write("Task done of emptying.")
