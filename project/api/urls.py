from django.urls import path

from . import views, stripe_views


app_name='api'


urlpatterns = [
    path(
        'buy/<int:pk>/',
        stripe_views.create_payment,
        name='create_payment'
    ),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
]
