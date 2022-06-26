from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name
