from django.conf import settings
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from stripe.checkout import Session as StripeSession

from .models import Item


def create_checkout_session(_: HttpRequest, pk: int) -> JsonResponse:
    '''
    API-интерфейс для создания Stripe-сессии по оплате Item, 
    выдаёт ответ {session_id: str}
    '''
    try:
        item = get_object_or_404(Item, pk=pk)
        checkout_session = StripeSession.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': int(item.price * 100),
                    },
                    'quantity': 1,
                }, 
            ],
            mode='payment',
            # success_url=reverse('api:item_detail', args=(pk,)),
            # cancel_url=reverse('api:item_detail', args=(pk,))
            success_url='https://ya.ru',
            cancel_url='https://ya.ru'
        )
        return JsonResponse({'session_id': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def item_detail(request: HttpRequest, pk: int) -> HttpResponse:
    '''
    Обзор и интерфейс для оплаты уже существующего предмета Item
    '''
    context = {
        'item': get_object_or_404(Item, pk=pk),
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }

    return render(request, 'api/item_detail.html', context=context)
