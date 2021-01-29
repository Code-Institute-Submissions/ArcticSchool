from django.db import models

# Create your models here.


class InstructorProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Instructors Profiles'

    name = models.CharField(max_length=254, blank=False)
    age = models.CharField(max_length=2, null=True, blank=False)
    about = models.TextField(null=True, blank=False)
    image = models.ImageField(upload_to="instructors",null=True, blank=True)

    def __str__(self):
        return self.name
