from django.http import HttpResponse, request


class StripeWH_Handler:
    """ This class will handle Stripe Webhooks """

    def __init__(self):
        self.request = request

    def handle_event(self, event):
        """ Handle a unknow/unexpected webhook event """

        return HttpResponse(
            content = f'Webhook received: {event["type"]}',
            status=200
        )