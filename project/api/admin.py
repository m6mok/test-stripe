from django.contrib import admin

from .models import Item, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price',)
    list_filter = ('name', 'price',)



class OrderAdmin(admin.ModelAdmin):
    list_display = ('created_at',)
    list_filter = ('created_at',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
