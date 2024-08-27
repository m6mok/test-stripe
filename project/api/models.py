from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from decimal import Decimal

from .enum import CurrencyChoices


class Item(models.Model):
    '''
    Модель для осуществления платежей по цене :price: в валюте USDT
    '''

    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    currency = models.CharField(
        max_length=3,
        choices=[(el.value, el.name) for el in CurrencyChoices],
        default='usd'
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Discount(models.Model):
    """
    Represents a discount that can be applied to an order.
    """
    name = models.CharField('Название', max_length=100)
    percentage = models.DecimalField('Процент скидки', max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name} ({self.percentage}%)'
    
    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Tax(models.Model):
    """
    Represents a tax that can be applied to an order.
    """
    name = models.CharField('Название', max_length=100)
    percentage = models.DecimalField('Процент налога', max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name} ({self.percentage}%)'
    
    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'


class Order(models.Model):
    '''
    Модель для представления заказа, состоящего из нескольких предметов Item
    '''
    items = models.ManyToManyField(
        Item,
        related_name='orders',
        verbose_name='Предметы'
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Скидка'
    )
    tax = models.ForeignKey(
        Tax,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Налог'
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self) -> str:
        return f'Order #{self.pk}'

    def total_price(self) -> float:
        '''
        Вычисляет общую стоимость всех предметов в заказе, 
        учитывая скидку и налог.
        '''
        total = float(sum(item.price for item in self.items.all()))
        if self.discount:
            total -= (total * float(self.discount.percentage) / 100)
        if self.tax:
            total += (total * float(self.tax.percentage) / 100)
        return float(total)

    def get_currency(self) -> CurrencyChoices:
        item: Item = self.items.first()
        return CurrencyChoices(item.currency)

    def clean(self):
        """
        Выполняет валидацию для Order 
        на общую валюту и неотрицательный результат.
        """
        items = self.items.all()
        if items and len(set(item.currency for item in items)) > 1:
            raise ValidationError(_(
                'Все товары в заказе должны иметь одну и ту же валюту.'
            ))

        total_price = self.total_price()
        if total_price <= Decimal('0'):
            raise ValidationError(_(
                'Общая стоимость заказа должна быть положительной.'
            ))

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
