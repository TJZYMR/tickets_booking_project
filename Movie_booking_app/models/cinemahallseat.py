from django.db import models
from Movie_booking_app.models.cinema import SeatType
from Movie_booking_app.models.cinemahall import CinemaHall
from Movie_booking_app.models.show import Show
from Movie_booking_app.models.statuses import SeatState
from django_extensions.db.fields import AutoSlugField

# 1.one cinema can have many seat Types=>done
# 2.one cinemahall can have multiple seat type=>done
# 3.one cinema hall can have multiple Cinema hall seats=>done


class CinemaHallSeat(models.Model):
    seatRow = models.CharField(max_length=100)
    seatColumn = models.CharField(max_length=100)
    seat_type = models.ForeignKey(SeatType, on_delete=models.CASCADE, null=True)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, null=True)
    seat_number = models.IntegerField()
    price = models.IntegerField(default=150, null=True)
    state = models.ForeignKey(SeatState, on_delete=models.CASCADE, null=True, default=2)
    # show = models.ForeignKey(Show, on_delete=models.CASCADE, null=True, default=1)
    # show_timing = models.ForeignKey(
    #     ShowTiming, on_delete=models.CASCADE, null=True, default=None
    # )

    slug = AutoSlugField(
        populate_from=["cinema_hall__slug"], unique=True, editable=True, default=""
    )

    def slugify_function(self, content):
        return content.replace(" ", "-").lower() + "-" + str(self.seat_number)

    def __str__(self):
        return str(self.slug)


class ShowWiseSeats(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, null=True, default=None)
    cinema_hall_seat = models.ForeignKey(
        CinemaHallSeat, on_delete=models.CASCADE, null=True
    )
    state = models.ForeignKey(SeatState, on_delete=models.CASCADE, null=True, default=2)

    class Meta:
        unique_together = ("show", "cinema_hall_seat", "state")

    def __str__(self):
        return (
            str(self.show)
            + "-"
            + "seat no.-"
            + str(self.cinema_hall_seat)
            + "-"
            + str(self.state)
        )
