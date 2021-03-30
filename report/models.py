from django.db import models
from django.contrib.postgres.fields import ArrayField


class WeatherInfo(models.Model):
    lat = models.DecimalField(max_digits=8, decimal_places=4)
    lon = models.DecimalField(max_digits=8, decimal_places=4)
    timezone = models.CharField(max_length=100, blank=True, null=True)
    timezone_offset = models.CharField(max_length=20, blank=True, null=True)
    minutely = ArrayField(models.CharField(max_length=100, blank=True, null=True), size=8)
    hourly = ArrayField(models.CharField(max_length=100, blank=True, null=True), size=8)
    daily = ArrayField(models.CharField(max_length=100, blank=True, null=True), size=8)

    class Meta:
        db_table = "weather"
