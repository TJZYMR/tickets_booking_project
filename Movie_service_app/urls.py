from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path


urlpatterns = [
    # path("register/", admin.site.urls),
    # path("login/", admin.site.urls),
    # path("password_reset/", admin.site.urls),
    # path("user_profile/", admin.site.urls),  # _with_slug_field
    # path("logout/", admin.site.urls),
    # path("book/", admin.site.urls),
    # path("movie/", admin.site.urls),
    # path("theatre/", admin.site.urls),
    # path("getCities/", admin.site.urls),
    # path("getTheatreByCity/", admin.site.urls),
    # path("getMovieByTheatre/", admin.site.urls),
    # path("getAuditoriumByMovie/", admin.site.urls),
    # path("getShowByAuditorium/", admin.site.urls),
    # path("sendticketbyemial/", admin.site.urls),
    # path("postcommentsandreview/", admin.site.urls),
    # path("getAvailableSeatByShows/", admin.site.urls),
    # path("admin_add_movie/", admin.site.urls),
    # path(
    #     "admin_delete_movie_or_shows/", admin.site.urls
    # ),  # using permission class or package
    # # -------------
    # path("search/", admin.site.urls),  # search by attributes TBD
    # path("search/", admin.site.urls),  # search by attributes TBD
    # path("search/", admin.site.urls),  # search by attributes TBD
    # path("search/", admin.site.urls),  # search by attributes TBD
    # path("search/", admin.site.urls),  # search by attributes TBD
    # path("search/", admin.site.urls),  # search by attributes TBD
    # path("search/", admin.site.urls),  # search by attributes TBD
    # path("search/", admin.site.urls),  # search by attributes TBD
    # path("search/", admin.site.urls),  # search by attributes TBD
]
