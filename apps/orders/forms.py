from clients.models import Client
from django.forms import CharField, Form, IntegerField, ModelMultipleChoiceField
from products.models import Product

from .models import Order


class OrderForm(Form):
    cliente = ModelMultipleChoiceField(queryset=Client.objects.all())
    order = Order.objects.all().last()
    ord = CharField(label="Número do pedido", disabled=True, initial=order.id + 1)
    produtos = ModelMultipleChoiceField(queryset=Product.objects.all())