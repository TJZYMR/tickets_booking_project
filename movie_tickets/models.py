from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Theatre(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    website = models.CharField(max_length=100,null=True)
    logo = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


class Screen(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Tier(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Seat(models.Model):
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
    status= models.CharField(max_length=100)
    price= models.CharField(max_length=100)
    show=
    # def __str__(self):
    #     return self.seat_no


class Movie(models.Model):
    screen = models.OneToOneField(Screen, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    trailer = models.CharField(max_length=100)
    release_date = models.DateField()
    duration = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    cast = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    awards = models.CharField(max_length=100)
    runtime = models.CharField(max_length=100)
    budget = models.CharField(max_length=100)
    revenue = models.CharField(max_length=100)
    imdb_rating = models.CharField(max_length=100)
    imdb_votes = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=100)
    tmdb_id = models.CharField(max_length=100)
    production_companies = models.CharField(max_length=100)
    production_countries = models.CharField(max_length=100)
    spoken_languages = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    homepage = models.CharField(max_length=100)
    adult = models.CharField(max_length=100)
    belongs_to_collection = models.CharField(max_length=100)
    homepage = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    original_language = models.CharField(max_length=100)
    popularity = models.CharField(max_length=100)
    vote_count = models.CharField(max_length=100)
    video = models.CharField(max_length=100)
    vote_average = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Offer(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.movie.name


class Ticket(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    tier = models.OneToOneField(Tier, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.seat.seat_no
