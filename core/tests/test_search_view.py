import mock

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import SearchResult
from .fixtures import city, features, searched_result


pytestmark = pytest.mark.django_db

search_url = reverse("search")


@mock.patch("requests.get")
def test_search_no_results_found(mock_usgs, client: APIClient, city):
    """Test search earthquakes for a city return no results"""
    mock_json = {"features": []}
    mock_usgs.return_value = mock.Mock(json=lambda: mock_json, status_code=200)
    usgs_search_params = f"start_date=2021-06-01&end_date=2021-07-01&city={city.id}"
    response = client.get(f"{search_url}?{usgs_search_params}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["title"] is None
    assert response.json()["earthquake_date"] is None


@mock.patch("requests.get")
def test_search_found_results(mock_usgs, client: APIClient, city):
    """Test search earthquakes for a city successfully"""
    mock_usgs.return_value = mock.Mock(json=lambda: features, status_code=200)

    assert SearchResult.objects.count() == 0

    usgs_search_params = f"start_date=2021-06-01&end_date=2021-06-05&city={city.id}"
    response = client.get(f"{search_url}?{usgs_search_params}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["title"] == "M 5.9 - 149 km W of Gold Beach, Oregon"
    assert response.json()["earthquake_date"] == "2021-06-04"
    assert SearchResult.objects.count() == 1


def test_search_found_searched_results(client: APIClient, city, searched_result):
    """Test search earthquakes for a city successfully with previous searched results"""
    usgs_search_params = f"start_date=2021-06-01&end_date=2021-06-05&city={city.id}"

    assert SearchResult.objects.count() == 1

    response = client.get(f"{search_url}?{usgs_search_params}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["title"] == "M 5.9 - 149 km W of Gold Beach, Oregon"
    assert response.json()["earthquake_date"] == "2021-06-04"
    assert SearchResult.objects.count() == 1


@pytest.mark.parametrize(
    "search_params,field",
    [
        ("start_date=2021-06-01&end_date=2021-06-05", "city"),
        ("start_date=2021-06-01&city=1", "end_date"),
        ("end_date=2021-06-05&city=1", "start_date"),
    ],
)
def test_search_missing_city_query_params(
    search_params, field, client: APIClient, city
):
    """Test search earthquakes for a city validation for missing parameters"""
    response = client.get(f"{search_url}?{search_params}")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()[field] == ["This field is required."]
    assert SearchResult.objects.count() == 0


def test_search_invalid_city_query_params(client: APIClient, city):
    """Test search earthquakes for an invalid city"""
    search_params = "start_date=2021-06-01&end_date=2021-06-05&city=999"
    response = client.get(f"{search_url}?{search_params}")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["city"] == ['Invalid pk "999" - object does not exist.']
    assert SearchResult.objects.count() == 0
