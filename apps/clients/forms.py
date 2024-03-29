from django.forms import ModelForm

from .models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["name", "phone", "address"]
        labels = {
            "name": ("Nome"),
            "phone": ("Telefone"),
            "address": ("Endereço"),
        }
