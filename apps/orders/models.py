from django.db import models


class Order(models.Model):
    client_id = models.ForeignKey("clients.Client", on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=100)
    obs = models.CharField(max_length=30)
    date = models.DateTimeField()

    def __str__(self):
        return self.client_id.name


class OrderItems(models.Model):
    item_id = models.ForeignKey("products.Item", on_delete=models.CASCADE)
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)
    extras = models.ForeignKey("OrderExtra", on_delete=models.CASCADE)

    def __str__(self):
        return self.item_id.name


class OrderExtra(models.Model):
    adicional_id = models.ForeignKey("products.Extra", on_delete=models.CASCADE)

    def __str__(self):
        return self.adicional_id.name
