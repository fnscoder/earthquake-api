from rest_framework.viewsets import ModelViewSet

from core.models import City
from core.serializers import CitySerializer


class CityModelViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
