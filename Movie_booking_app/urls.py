from django.urls import include, path, re_path
from Movie_booking_app.views import *
from rest_framework.routers import DefaultRouter
from django.urls import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from Movie_booking_app.views import *

# router = DefaultRouter()
# router.register(r"registration", UserViewSet, basename="registration")
# router.register(r"profile", UserViewSet, basename="profile")
# router.register(r"cinemas", CinemaViewSet, basename="cinema")
# router.register(r"cinemahalls", CinemaHallViewSet, basename="cinemahall")
# router.register(r"cinemahallseats", CinemaHallSeatViewSet, basename="cinemahallseat")
# router.register(r"movies", MovieViewSet, basename="movie")
# router.register(r"shows", ShowViewSet, basename="show")
# router.register(r"bookings", BookingViewSet, basename="booking")
# router.register(r"seattypes", SeatTypeViewSet, basename="seattype")
# router.register(r"seats", SeatTypeViewSet, basename="seat")
# router.register(r"paymentstatuses", PaymentStatusViewSet, basename="paymentstatus")
# router.register(r"bookingstatuses", BookingStatusViewSet, basename="bookingstatus")
# router.register(r"accountstatuses", AccountStatusViewSet, basename="accountstatus")
# router.register(r"notifications", NotificationViewSet, basename="notification")
# router.register(
#     r"notificationtypes", NotificationTypeViewSet, basename="notificationtype"
# )


urlpatterns = [
    path("registration/", UserViewSet.as_view({"post": "create"}), name="registration"),
    path(
        "profile/<str:slug>/", UserViewSet.as_view({"get": "retrieve"}), name="profile"
    ),
    path("login/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    re_path(r"^auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.jwt")),
    path("movie/", MovieViewSet.as_view({"get": "list"}), name="movie"),
    # cinemawise list of all shows in that cinema
    path(
        "shows/cinema",
        ShowViewSet.as_view({"get": "retrieve"}),
        name="shows_cinemawise",
    ),
    path(
        "shows/movie",
        CinemaViewSet.as_view({"get": "retrieve"}),
        name="shows_location_and_moviewise",
    ),
    path("booking/", BookViewSet.as_view({"post": "create"}, name="booking")),
]

# authentication urls
# /users/
# /users/me/
# /users/confirm/
# /users/resend_activation/
# /users/set_password/
# /users/reset_password/
# /users/reset_password_confirm/
# /users/set_username/
# /users/reset_username/
# /users/reset_username_confirm/
# /token/login/ (Token Based Authentication)#not used here
# /token/logout/ (Token Based Authentication)#not used here beacuse we used jwt auth with access and refresh tokens
# /jwt/create/ (JSON Web Token Authentication)
# /jwt/refresh/ (JSON Web Token Authentication)
# /jwt/verify/ (JSON Web Token Authentication)
# urlpatterns += router.urls
