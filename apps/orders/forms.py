from clients.models import Client
from django.forms import CharField, Form, ModelMultipleChoiceField
from products.models import Product

from .models import Order


class ClientForm(Form):
    cliente = ModelMultipleChoiceField(queryset=Client.objects.all())


class OrderForm(Form):
    order = Order.objects.all().last()
    ord = CharField(label="order", disabled=True, initial=order.id + 1)


class OrderProductForm(Form):
    order = ModelMultipleChoiceField(queryset=Product.objects.all())
    quantity = CharField(label="quantity")