import requests
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import WeatherInfo
from django.db import transaction
from django.db import DatabaseError
import django
from rest_framework import viewsets
from .serializers import WeatherSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def store_data(request,lat,lon,detailing):

    print("lat",lat)
    print("lon",lon)
    print("detailing",detailing)

    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=28.7041&lon=77.1025&exclude=current&appid' \
        '=676d95b33a0d70d28ff022f4cf88efb6'
    response = requests.get(url)
    api_data = response.json()

    minutely = api_data['minutely']
    # item = next(item['dt'] for item in minutely if 'dt' in item)
    # print("item",item)

    already_has_data = WeatherInfo.objects.filter(lat=lat, lon=lon)
    print("already_has_data",len(already_has_data))
    if len(already_has_data) > 0:
        print("data already store in db")
    else:
        # try:
        print("else insertdata")
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

        # except:
        #     pass
    # return JsonResponse(api_data)
    # queryset = WeatherInfo.objects.all()
    serializer = WeatherSerializer(already_has_data, many=True)
    return JsonResponse(serializer.data, safe=False)




# @csrf_exempt
# def Weather(request):
#     queryset = WeatherInfo.objects.all()
#     print("q",queryset)
#     serializer = WeatherSerializer(queryset,many=True)
#     print("ss",serializer)
#     return JsonResponse(serializer.data,safe=False)
