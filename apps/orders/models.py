from django.db import models


class Order(models.Model):
    client_id = models.ForeignKey("clients.Client", on_delete=models.CASCADE)
    obs = models.CharField(max_length=30)
    date = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.client_id.name


class OrderItem(models.Model):
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)
    item_id = models.ForeignKey("products.Item", on_delete=models.CASCADE)

    def __str__(self):
        return self.item_id.name


class ItemExtra(models.Model):
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)
    item_id = models.ForeignKey("products.Item", on_delete=models.CASCADE)
    extra_id = models.ForeignKey("products.Extra", on_delete=models.CASCADE)

    def __str__(self):
        return self.extra_id.name
