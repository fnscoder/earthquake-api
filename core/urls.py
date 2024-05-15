from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import CityModelViewSet, EarthquakeSearchViewSet

router = DefaultRouter()

router.register("cities", CityModelViewSet, "city")

urlpatterns = [
    path("", include(router.urls)),
    path("search/", EarthquakeSearchViewSet.as_view({"get": "list"}), name="search"),
]
