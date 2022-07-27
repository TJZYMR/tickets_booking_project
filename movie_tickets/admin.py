from django.contrib import admin
from .models import User, Ticket, Offer, Movie, Screen, Theatre, Tier, Seat, Place

# Register your models here.
admin.site.register([Ticket, Offer, Movie, Screen, Theatre, Tier, Seat, Place])
