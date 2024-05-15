from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import City, SearchResult


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

    def validate_lat(self, value):
        if value < -90 or value > 90:
            raise ValidationError('Latitude must be between -90 and 90 degrees.')
        return value

    def validate_long(self, value):
        if value < -180 or value > 180:
            raise ValidationError('Longitude must be between -180 and 180 degrees.')
        return value


class SearchResultSerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())

    class Meta:
        model = SearchResult
        fields = "__all__"
