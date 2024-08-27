from django.db import models


class Item(models.Model):
    '''
    Модель для осуществления платежей по цене :price: в валюте USDT
    '''
    
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
