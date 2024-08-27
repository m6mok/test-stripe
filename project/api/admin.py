from django.contrib import admin

from .models import Item, Order, Discount, Tax


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'currency',)
    list_filter = ('name', 'price', 'currency',)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'total_items',
        'total_price',
        'currency',
        'discount_name',
        'discount_percentage',
        'tax_name',
        'tax_percentage',
    )
    list_filter = (
        'created_at',
        'discount',
        'tax',
    )

    def total_items(self, obj: Order) -> int:
        return obj.items.count()

    def total_price(self, obj: Order) -> float:
        return round(obj.total_price(), 2)

    def currency(self, obj: Order) -> str:
        return obj.get_currency().name

    def discount_name(self, obj: Order) -> str:
        return obj.discount.name if obj.discount else 'No Discount'

    def discount_percentage(self, obj: Order) -> float | str: 
        return obj.discount.percentage if obj.discount else 'N/A'

    def tax_name(self, obj: Order) -> str:
        return obj.tax.name if obj.tax else 'No Tax'

    def tax_percentage(self, obj: Order) -> float | str:
        return obj.tax.percentage if obj.tax else 'N/A'

    total_items.short_description = 'Количество Товаров'
    total_price.short_description = 'Итоговая сумма'
    currency.short_description = 'Валюта'
    discount_name.short_description = 'Название скидки'
    discount_percentage.short_description = 'Скидка'
    tax_name.short_description = 'Название налога'
    tax_percentage.short_description = 'Налог'


class DiscountAndTaxAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage',)
    list_filter = ('name', 'percentage',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register((Discount, Tax), DiscountAndTaxAdmin)
