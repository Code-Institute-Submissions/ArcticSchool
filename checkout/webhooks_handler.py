from django.http import HttpResponse, request


class StripeWebhooks_Handler:
    """ This class will handle Stripe Webhooks """

    def __init__(self):
        self.request = request

    def handle_event(self, event):
        """ Handle a unknow/unexpected webhook event """

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_succeeded_payment(self, event):
        """ Handle payment intent when succeeded from Stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_failed_payment(self, event):
        """ Handle payment intent when failed from Stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
