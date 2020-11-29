from typing import Text
from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Resort(models.Model):

    name = models.CharField(max_length=120, default='Resort Name')
    country = CountryField(blank_label="(Select Country)")
    address = models.CharField(max_length=80)
    about = models.TextField(default="Some text about resort")
    levels = models.TextField(
        default="Type levels as example: Beginner, Intermediate, Advance, etc.")
    styles = models.TextField(
        default="Type styles as example: Freestyle Riding, Carving, Off-Psite, etc.")
    instructors = models.IntegerField(default=0)
    map_link = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to="resorts",null=True, blank=True)

    def __str__(self):
        return self.name
