from django.db import models


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey("clients.Client", on_delete=models.CASCADE)
    obs = models.CharField(max_length=30)
    date = models.DateTimeField(auto_created=True, auto_now=True)
    products = models.ManyToManyField("products.Product", related_name="orders")

    def __str__(self):
        return str(self.id)
