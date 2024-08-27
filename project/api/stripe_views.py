from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404
from stripe import (
    PaymentIntent as StripePaymentIntent
)

from .models import Order


def create_payment(_: HttpRequest, pk: int) -> JsonResponse:
    '''
    API-интерфейс для создания Stripe-сессии по оплате Order, 
    выдаёт ответ {client_secret: str}
    '''
    order = get_object_or_404(Order, pk=pk)
    currency = order.get_currency()

    return JsonResponse({
        'client_secret': StripePaymentIntent.create(
            amount=int(order.total_price() * 100),
            currency=currency.value,
            payment_method_types=['card']
        ).client_secret
    })
