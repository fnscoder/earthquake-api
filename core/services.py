from datetime import datetime
import logging

from haversine import haversine
import requests

from core.models import SearchResult
from earthquake.settings import USGS_API_URL, MIN_MAGNITUDE


logger = logging.getLogger(__name__)


class EarthquakeService:
    def fetch_earthquake_data(self, data):
        """
        Function to fetch earthquake data from USGS API.
        """
        usgs_search_params = {
            "starttime": data["start_date"],
            "endtime": data["end_date"],
            "minmagnitude": MIN_MAGNITUDE
        }
        response = requests.get(USGS_API_URL, params=usgs_search_params)
        response.raise_for_status()

        return response.json().get("features", [])

    def find_nearest_earthquake(self, earthquakes, data):
        """
        Finds the nearest earthquake to a given data (city, start_date and end_date).
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
            try:
                eq_lat = earthquake["geometry"]["coordinates"][1]
                eq_long = earthquake["geometry"]["coordinates"][0]
                distance = haversine((eq_lat, eq_long), (city.lat, city.long))
                if distance < nearest_distance:
                    nearest_distance = distance
                    timestamp = earthquake["properties"]["time"]
                    earthquake_data["earthquake_date"] = datetime.fromtimestamp(timestamp / 1000).date()
                    earthquake_data["title"] = earthquake["properties"]["title"]
            except KeyError as e:
                logger.error(f"Error when processing earthquake data: {e}")

        return earthquake_data

    def get_nearest_earthquake(self, data):
        """
        Retrieve the nearest earthquake information based on the given data.
        """
        try:
            earthquakes = self.fetch_earthquake_data(data)
        except requests.exceptions.RequestException as e:
            logger.error(f"Error occurred while fetching data from USGS API: {e}")
            return

        nearest_earthquake_data = self.find_nearest_earthquake(earthquakes, data)
        return SearchResult.objects.create(**nearest_earthquake_data)
