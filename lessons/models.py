from django.db import models
from home.models import LevelCard
from resorts.models import Resort


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.category

    def __str__(self):
        return self.friendly_name


class Lesson(models.Model):
    name = models.CharField(max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.PROTECT)
    level = models.ForeignKey(
        LevelCard, null=True, blank=True, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    participants = models.IntegerField(null=True, blank=True)
    resort = models.ForeignKey(
        Resort, null=True, blank=True, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True)
    supper_offer = models.BooleanField(null=True, blank=True, default=False)
    image = models.ImageField(upload_to="lessons",null=True, blank=True)

    def __str__(self):
        return self.name