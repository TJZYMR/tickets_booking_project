from django.db import models
from Movie_booking_app.models.cinema import SeatType

from Movie_booking_app.models.cinemahall import CinemaHall

# 1.one cinema can have many seat Types=>done
# 2.one cinemahall can have multiple seat type=>done
# 3.one cinema hall can have multiple Cinema hall seats=>done
class CinemaHallSeat(models.Model):
    seatRow = models.CharField(max_length=100)
    seatColumn = models.CharField(max_length=100)
    seat_type = models.ForeignKey(SeatType, on_delete=models.CASCADE, null=True)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, null=True)
    seat_number = models.IntegerField()

    def __str__(self):
        return self.seat_number
