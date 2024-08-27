from django.db import models


class Item(models.Model):
    '''
    Модель для осуществления платежей по цене :price: в валюте USDT
    '''
    
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    '''
    Модель для представления заказа, состоящего из нескольких предметов Item
    '''
    items = models.ManyToManyField(Item, related_name='orders', verbose_name='Предметы')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self) -> str:
        return f'Order #{self.pk}'

    def total_price(self) -> float:
        '''
        Вычисляет общую стоимость всех предметов в заказе.
        '''
        return sum(item.price for item in self.items.all())
