import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import City

pytestmark = pytest.mark.django_db


city_data = {
    "name": "Los Angeles",
    "state": "CA",
    "country": "USA",
    "lat": 34.0522,
    "long": -118.2437,
}

url_list = reverse("city-list")


def test_create_city_successful(client: APIClient):
    """Test create a city via API successfully"""
    response = client.post(url_list, city_data)

    assert response.status_code == 201


def test_create_city_validation_error(client: APIClient):
    """Test create a city via API raise error when missing required info"""
    data = {
        "state": "CA",
        "country": "USA",
        "lat": 34.0522,
        "long": -118.2437,
    }

    response = client.post(url_list, data)

    assert response.status_code == 400
    assert response.json()["name"][0] == "This field is required."


def test_create_city_validation_error_invalid_lat_and_long(client: APIClient):
    """Test create a city via API raise error when wrong lat and long"""
    data = {
        "name": "City Name",
        "state": "CA",
        "country": "USA",
        "lat": 134.0522,
        "long": -218.2437,
    }

    response = client.post(url_list, data)

    assert response.status_code == 400
    assert response.json()["lat"][0] == "Latitude must be between -90 and 90 degrees."
    assert response.json()["long"][0] == "Longitude must be between -180 and 180 degrees."


def test_retrieve_cities_list_successful(client: APIClient):
    """Test retrieve all the cities via API successfully"""
    for i in range(1, 5):
        city_data["name"] = f"{city_data['name']} - {i}"
        City.objects.create(**city_data)

    response = client.get(url_list)

    assert response.status_code == 200
    assert len(response.json()) == City.objects.count()


def test_retrieve_city_detail(client: APIClient):
    """Test get a city detail via API successfully"""
    city = City.objects.create(**city_data)
    url = reverse("city-detail", kwargs={"pk": city.id})

    response = client.get(url)

    assert response.status_code == 200
    assert response.json()["name"] == city.name


def test_update_city(client: APIClient):
    """Test update a city detail via API successfully"""
    city = City.objects.create(**city_data)
    url = reverse("city-detail", kwargs={"pk": city.id})

    city_data["state"] = "California"

    response = client.put(url, city_data, content_type="application/json")

    assert response.status_code == 200
    assert response.json()["state"] == "California"


def test_partial_update_city(client: APIClient):
    """Test partially update a city detail via API successfully"""
    city = City.objects.create(**city_data)
    url = reverse("city-detail", kwargs={"pk": city.id})

    new_data = {"country": "United States of America"}

    response = client.patch(url, new_data, content_type="application/json")

    assert response.status_code == 200
    assert response.json()["country"] == "United States of America"


def test_delete_city(client: APIClient):
    """Test delete a city via API successfully"""
    city = City.objects.create(**city_data)
    url = reverse("city-detail", kwargs={"pk": city.id})

    response = client.delete(url)

    assert response.status_code == 204
    assert City.objects.filter(id=city.id).exists() is False
