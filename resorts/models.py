from typing import Text
from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Resort(models.Model):

    name = models.CharField(max_length=120)
    country = CountryField(max_length=200, blank_label="(Select Country)")
    about = models.TextField(max_length=500)
    open_season = models.CharField(max_length=120, default="December - April")
    top_altitude = models.IntegerField(default=0)
    bottom_altitude = models.IntegerField(default=0)
    resort_altitude = models.IntegerField(default=0)
    levels = models.TextField()
    instructors = models.IntegerField(default=0)
    image = models.ImageField(upload_to="resorts", null=True, blank=True)

    def __str__(self):
        return self.name
