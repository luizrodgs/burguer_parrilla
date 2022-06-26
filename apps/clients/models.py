from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name
