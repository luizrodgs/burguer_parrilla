from django.contrib import admin

from .models import Order, OrderExtra, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderExtra)
