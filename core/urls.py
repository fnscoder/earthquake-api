from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import CityModelViewSet

router = DefaultRouter()

router.register("cities", CityModelViewSet, "city")

urlpatterns = [
    path("", include(router.urls)),
]
