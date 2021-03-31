from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField


class WeatherInfo(models.Model):
    lat = models.DecimalField(max_digits=8, decimal_places=4)
    lon = models.DecimalField(max_digits=8, decimal_places=4)
    timezone = models.CharField(max_length=100, blank=True, null=True)
    timezone_offset = models.CharField(max_length=20, blank=True, null=True)
    # minutely = JSONField(models.CharField(max_length=100, blank=True, null=True))
    # hourly = JSONField(models.CharField(max_length=100, blank=True, null=True))
    # daily = JSONField(models.CharField(max_length=100, blank=True, null=True))
    minutely = JSONField(null=True, blank=True)
    hourly = JSONField(null=True, blank=True)
    daily = JSONField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "weather"

