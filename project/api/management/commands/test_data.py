from django.core.management.base import BaseCommand

from api.models import Item, Order, Discount, Tax


class Command(BaseCommand):
    help = 'Создает тестовые данные для моделей API'

    def handle(self, *args, **kwargs):
        if Order.objects.count() > 0:
            self.stdout.write(self.style.SUCCESS(
                'Тестовый Заказ не был добавлен. В Базе уже имеются Заказы.'
            ))
            return

        items = (
            Item(name='Сапоги', description='Практичный вариант обуви', price=10.00, currency='usd'),
            Item(name='Туфли', description='Красивый вариант обуви', price=20.00, currency='usd'),
            Item(name='Картошка', description='Съедобный товар', price=3.00, currency='usd'),
            Item(name='Платье', description='Красивый товар', price=20.00, currency='eur'),
        )

        if Item.objects.count() == 0:
            for item in items:
                item.save()
        else:
            items = []

        self.stdout.write(
            self.style.SUCCESS(
                f'Добавлено тестовых Товаров: {len(items)}'
            )
        )

        discounts = (
            Discount(name='Скидка на День Рождения', percentage=10.00),
            Discount(name='Скидка постоянного покупателя', percentage=7.00),
        )

        if Discount.objects.count() == 0:
            for discount in discounts:
                discount.save()
        else:
            discounts = []

        self.stdout.write(
            self.style.SUCCESS(
                f'Добавлено тестовых Скидок: {len(discounts)}'
            )
        )

        taxes = (
            Tax(name='УСН Доходы', percentage=6.00),
            Tax(name='УСН Доходы минус расходы', percentage=15.00),
        )

        if Tax.objects.count() == 0:
            for tax in taxes:
                tax.save()
        else:
            taxes = []    
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Добавлено тестовых Налогов: {len(taxes)}'
            )
        )

        order = Order.objects.create(created_at='2024-08-27 12:00:00')
        order.items.set(items[:3])
        if discounts:
            order.discount = discounts[0]
        if taxes:
            order.tax = taxes[0]
        order.clean()
        order.save()

        self.stdout.write(self.style.SUCCESS('Добавлен тестовый Заказ'))

