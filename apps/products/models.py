from django.db import models


class Aditional(models.Model):
    name = models.FloatField()
    price = models.FloatField()


class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    price = models.FloatField()
