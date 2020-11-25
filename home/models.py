from django.db import models

# Create your models here.


class Levels(models.Model):
    class levelChoices(models.TextChoices):
        Level_1 = '1',
        Level_2 = '2',
        Level_3 = '3',
        Level_4 = '4'


    title = models.TextField(max_length=40)
    level = models.CharField(choices=levelChoices.choices, default=levelChoices.Level_1, max_length=1)
    description = models.TextField(max_length=130)
