from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Order


def order_detail(request: HttpRequest, pk: int) -> HttpResponse:
    '''
    Обзор и интерфейс для оплаты уже существующего предмета Item
    '''
    order = get_object_or_404(Order, pk=pk)

    context = {
        'order': order,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'currency_name': order.get_currency().name
    }

    return render(request, 'api/order_detail.html', context=context)
