import requests
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import WeatherInfo
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import WeatherSerializer


def store_data(request):

    lat = request.GET['lat']
    lon = request.GET['lon']
    detailing = request.GET['detailing']
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lon+'&exclude='+detailing+'&appid' \
        '=676d95b33a0d70d28ff022f4cf88efb6'
    response = requests.get(url)
    api_data = response.json()
    already_has_data = WeatherInfo.objects.filter(lat=lat, lon=lon)

    if len(already_has_data) > 0:
        print("data already store in db")
    else:
        insert_data = WeatherInfo(
            lat=lat,
            lon=lon,
            timezone=api_data['timezone'],
            timezone_offset=api_data['timezone_offset'],
            minutely=api_data['minutely'],
            hourly=api_data['hourly'],
            daily=api_data['daily'],
        )
        insert_data.save()

    serializer = WeatherSerializer(already_has_data, many=True)
    return JsonResponse(serializer.data, safe=False)




# def Weather(request):
#     queryset = WeatherInfo.objects.all()
#     serializer = WeatherSerializer(queryset,many=True)
#     return JsonResponse(serializer.data,safe=False)
