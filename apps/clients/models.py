from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)


class Order(models.Model):
    client_id = models.ForeignKey("Client", on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=100)
    obs = models.CharField(max_length=30)
    date = models.DateTimeField()
    status = models.CharField(max_length=30)


class OrderItems(models.Model):
    item_id = models.ForeignKey("Item", on_delete=models.CASCADE)
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)
    aditional_list_id = models.ForeignKey("AditionalList", on_delete=models.CASCADE)


class Aditional(models.Model):
    name = models.FloatField()
    price = models.FloatField()


class AditionalList(models.Model):
    adicional_id = models.ForeignKey("Aditional", on_delete=models.CASCADE)



class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    price = models.FloatField()
