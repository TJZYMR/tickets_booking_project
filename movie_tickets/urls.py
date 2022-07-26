from django.contrib import admin
from django.urls import path, include


def test(request):
    division = 1 / 0


urlpatterns = [
    path("test/", test),
]
