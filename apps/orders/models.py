from django.db import models


class Order(models.Model):
    client_id = models.ForeignKey("clients.Client", on_delete=models.CASCADE)
    obs = models.CharField(max_length=30)
    date = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.client_id.name


class OrderProduct(models.Model):
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)
    product_id = models.ForeignKey("products.Product", on_delete=models.CASCADE)

    def __str__(self):
        return self.product_id.name
