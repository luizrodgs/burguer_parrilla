from datetime import datetime

from clients.models import Client
from django.forms import (
    CharField,
    DateTimeField,
    Form,
    ModelMultipleChoiceField,
    Textarea,
)
from products.models import Product

from .models import Order


class OrderForm(Form):
    order = Order.objects.all().last()

    if order:
        order_id = order.id + 1
    else:
        order_id = 1

    ord = CharField(label="Número do pedido:", disabled=True, initial=order_id)
    date = DateTimeField(label="Data do pedido:", disabled=True, initial=datetime.today)
    client = ModelMultipleChoiceField(queryset=Client.objects.all(), label="Cliente")
    products = ModelMultipleChoiceField(
        queryset=Product.objects.all(), label="Produtos"
    )
    obs = CharField(
        label="Observação:", max_length=300, required=False, widget=Textarea
    )
