from django.urls import path

from . import views


app_name='api'


urlpatterns = [
    path(
        'buy/<int:pk>/',
        views.create_checkout_session,
        name='create_checkout_session'
    ),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
]
