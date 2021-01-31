""" Checkout App Configuration """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ Checkout App Name """
    name = 'checkout'

    def ready(self):
        import checkout.signals
