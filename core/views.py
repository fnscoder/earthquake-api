from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from core.models import City, SearchResult
from core.serializers import CitySerializer, SearchResultSerializer
from core.services import EarthquakeService


class CityModelViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class EarthquakeSearchViewSet(ViewSet):

    def find_existing_search_result(self, validated_data):
        """
        Find an existing search result by city, start date, and end date.
        """
        return SearchResult.objects.filter(**validated_data).first()

    def get_search_result(self, data):
        """
        Gets the search result based on the given data.
        """
        existing_search_result = self.find_existing_search_result(data)

        if existing_search_result:
            return existing_search_result

        service = EarthquakeService()
        new_search_result = service.get_nearest_earthquake(data)

        return new_search_result

    def list(self, request):
        """
        Receives a GET request, validates received data, fetches earthquake data,
        finds the nearest earthquake, saves the result and returns it.
        """
        serializer = SearchResultSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)

        search_result = self.get_search_result(serializer.validated_data)

        serializer = SearchResultSerializer(search_result)
        return Response(serializer.data)
