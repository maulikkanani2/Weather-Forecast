from rest_framework import serializers
from .models import WeatherInfo


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherInfo
        fields = ('lat', 'lon', 'timezone', 'timezone_offset', 'minutely', 'hourly', 'daily')