from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.


class InstructorProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Instructors Profiles'

    name = models.CharField(max_length=254)
    age = models.CharField(max_length=2)
    about = models.TextField(max_length=1024)
    riding_style = models.CharField(max_length=100)
    favourite_trick = models.TextField(max_length=100)
    qualifications = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
