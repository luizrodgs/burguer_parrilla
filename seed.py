import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

import random

from clients.models import Client
from faker import Faker


def creating_clients(quantidade_de_pessoas):
    fake = Faker("pt_BR")
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        name = fake.name()
        phone = "{}{} 9{}{}{}{}-{}{}{}{}".format(
            random.randrange(1, 10),
            random.randrange(1, 10),
            random.randrange(8, 10),
            random.randrange(0, 10),
            random.randrange(0, 10),
            random.randrange(0, 10),
            random.randrange(0, 10),
            random.randrange(0, 10),
            random.randrange(0, 10),
            random.randrange(0, 10),
        )
        address = ""
        a = Client(name=name, phone=phone, address=address)
        a.save()


creating_clients(200)
