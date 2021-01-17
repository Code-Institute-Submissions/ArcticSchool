import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from lessons.models import Lesson


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _create_order_number(self):
        """ This function will create a random, unique order number by using UUID """
        return uuid.uuid4().hex.upper

    def update_total(self):
        """ Update grand total when new item is added, include discount. """

        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))[
            'lineitem_total__sum']
        if self.order_total > settings.OFF_DISCOUNT_THRESHOLD:
            self.discount = self.order_total * settings.OFF_DISCOUNT/100
        else:
            self.discount = 0
        self.grand_total = self.order_totaltotal - self.discount
        self.save()

    def save(self, *args, **kwargs):
        """ This function will override the orignal save method and
        create the order number if it hasn't been created before """

        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='lineitems')
    lesson = models.ForeignKey(
        Lesson, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """ This functiojn will override the orignal save method to set the
         """

        self.lineitem_total = self.lesson.price * self.quantity
        super().save(*args, **kwargs)