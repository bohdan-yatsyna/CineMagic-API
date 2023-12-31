from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieSessionViewSet,
    MovieViewSet,
    OrderViewSet,
)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet, basename="actor")
router.register("cinema_halls", CinemaHallViewSet, basename="cinemahall")
router.register("genres", GenreViewSet, basename="genre")
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="moviesession"
)
router.register("orders", OrderViewSet, basename="order")

urlpatterns = [path("", include(router.urls))]

app_name = "cinema"
