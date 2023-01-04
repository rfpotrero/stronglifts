from django.http import HttpResponse


class StripeWH_Handler:
    """Handle for stripe webhooks"""
    
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Generic handle event """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle succeeded payment event payment_intent.succeeded from Stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """ Handle succeeded payment event payment_intent.failed from Stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)