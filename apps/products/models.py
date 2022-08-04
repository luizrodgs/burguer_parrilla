from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return str(self.name)
