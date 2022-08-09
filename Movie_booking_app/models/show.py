# from this import s
from django_extensions.db.fields import AutoSlugField
from django.db import models
from Movie_booking_app.models.cinema import Cinema
from Movie_booking_app.models.cinemahall import CinemaHall
from Movie_booking_app.models.movie import Movie

# from Movie_booking_app.models.cinema import Cinema


# 1.a movie can have multiple shows=>done
# 2.a cinemahall can have one movie at a time.=>done
# 3.one cinema can have manyshows.=>done


class Show(models.Model):
    created_on = models.DateField(auto_now_add=True)
    date = models.DateField(null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True)
    cinema_hall = models.ForeignKey(
        CinemaHall, on_delete=models.CASCADE, null=True  # , related_name="shows_hall"
    )
    is_active = models.BooleanField(default=True)
    total_seats = models.IntegerField(default=50, null=True)
    available_seats = models.IntegerField(default=50, null=True)
    # price = models.IntegerField(default=0)
    # cinemahallseat = models.ForeignKey(
    #     CinemaHallSeat, on_delete=models.CASCADE, null=True
    # )
    # timing = models.CharField(max_length=50, null=True)
    slug = AutoSlugField(
        populate_from=["movie__slug"], unique=True, editable=True, default=""
    )

    def slugify_function(self, content):
        if self.start_time.hour < 12:
            show_shift = "Morning"
        elif self.start_time.hour < 18:
            show_shift = "Afternoon"
        elif self.start_time.hour < 20:
            show_shift = "Evening"
        else:
            show_shift = "Night"
        return (
            content.replace(" ", "-").lower()
            + "-"
            + str(self.date)
            + "-"
            + show_shift
            + "-show"
        )

    def __str__(self):
        return self.slug

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "date",
                    "start_time",
                    "end_time",
                    "movie",
                    "cinema_hall",
                    "cinema",
                ],
                name="unique show",
            )
        ]


# class SeatShow(models.Model):
#     seat_no = models.ForeignKey(CinemaHallSeat, on_delete=models.CASCADE, null=True)
#     show = models.OneToOneField(Show, verbose_name=("ID"), primary_key=True)
