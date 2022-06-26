from django.contrib import admin

from .models import ItemExtra, Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ItemExtra)
