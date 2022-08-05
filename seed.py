import os

import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from clients.models import Client


def creating_clients(number_of_clients):
    fake = Faker("pt_BR")
    Faker.seed(10)
    for _ in range(number_of_clients):
        name = fake.name()
        phone = fake.cellphone_number()
        address = fake.address()
        client = Client(name=name, phone=phone, address=address)
        client.save()


if __name__ == "__main__":
    creating_clients(200)
