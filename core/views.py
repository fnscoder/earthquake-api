from datetime import datetime

from haversine import haversine
import requests
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from core.models import City, SearchResult
from core.serializers import CitySerializer, SearchResultSerializer
from earthquake.settings import USGS_API_URL, MIN_MAGNITUDE


class CityModelViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class EarthquakeSearchViewSet(ViewSet):

    def find_existing_search_result(self, validated_data):
        """
        Find an existing search result by city, start date, and end date.
        """
        return SearchResult.objects.filter(**validated_data).first()

    def generate_response(self, search_result):
        """
        Generate a response based on the given search result.
        If the earthquake_date field is null, no results were found during those dates
        """
        if not search_result.earthquake_date:
            return "No results found"

        city = search_result.city
        start_date = search_result.start_date.strftime('%B %d %Y')
        end_date = search_result.end_date.strftime('%B %d %Y')
        title = search_result.title
        earthquake_date = search_result.earthquake_date.strftime('%B %d %Y')

        return (
            f"Result for {city} between {start_date} and {end_date} : "
            f"The closest Earthquake to {city} was a {title} on {earthquake_date}"
        )

    def fetch_earthquake_data(self, validated_data):
        """
        Function to fetch earthquake data from USGS API.
        """
        usgs_search_params = {
            "starttime": validated_data["start_date"],
            "endtime": validated_data["end_date"],
            "minmagnitude": MIN_MAGNITUDE
        }
        response = requests.get(USGS_API_URL, params=usgs_search_params)
        response.raise_for_status()
        return response.json()["features"]

    def find_nearest_earthquake(self, earthquakes, data):
        """
        Finds the nearest earthquake to a given city.
        """
        city = data["city"]
        earthquake_data = {
            "city": city,
            "start_date": data["start_date"],
            "end_date": data["end_date"],
            "earthquake_date": None,
            "title": None,
        }

        nearest_distance = float("inf")
        for earthquake in earthquakes:
            eq_lat = earthquake["geometry"]["coordinates"][1]
            eq_long = earthquake["geometry"]["coordinates"][0]
            distance = haversine((eq_lat, eq_long), (city.lat, city.long))

            if distance < nearest_distance:
                nearest_distance = distance
                timestamp = earthquake["properties"]["time"]
                earthquake_data["earthquake_date"] = datetime.fromtimestamp(timestamp / 1000).date()
                earthquake_data["title"] = earthquake["properties"]["title"]

        return earthquake_data

    def list(self, request):
        """
        Receives a GET request, validates received data, fetches earthquake data,
        finds the nearest earthquake, saves the result and returns it.
        """
        serializer = SearchResultSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)

        existing_search_result = self.find_existing_search_result(serializer.validated_data)

        if existing_search_result:
            earthquake_response = self.generate_response(existing_search_result)

            return Response(earthquake_response)

        earthquakes = self.fetch_earthquake_data(serializer.validated_data)
        nearest_earthquake_data = self.find_nearest_earthquake(earthquakes, serializer.validated_data)
        search_result = SearchResult.objects.create(**nearest_earthquake_data)
        earthquake_response = self.generate_response(search_result)

        return Response(earthquake_response)
