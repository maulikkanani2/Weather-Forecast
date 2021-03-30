import requests
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import WeatherInfo
from django.db import transaction
from django.db import DatabaseError
import django


def store_data(request):
    response = requests.get(
        'https://api.openweathermap.org/data/2.5/onecall?lat=22.2587&lon=71.1924&exclude=current&appid'
        '=676d95b33a0d70d28ff022f4cf88efb6')
    api_data = response.json()
    lat = api_data['lat']
    lon = api_data['lon']
    minutely = api_data['minutely'],
    hourly = api_data['hourly'],
    daily = api_data['daily'],
    try:
        insert_data = WeatherInfo(
            lat=lat,
            lon=lon,
            timezone=api_data['timezone'],
            timezone_offset=api_data['timezone_offset'],
            minutely=minutely,
            hourly=hourly,
            daily=daily,
        )
        insert_data.save()

    except django.db.utils.DatabaseError as e:
        print(e)
    return JsonResponse(api_data)

