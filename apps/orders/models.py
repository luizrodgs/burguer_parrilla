from django.db import models


class Order(models.Model):
    client_id = models.ForeignKey("clients.Client", on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=100)
    obs = models.CharField(max_length=30)
    date = models.DateTimeField()
    status = models.CharField(max_length=30)


class OrderItems(models.Model):
    item_id = models.ForeignKey("products.Item", on_delete=models.CASCADE)
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)
    aditional_list_id = models.ForeignKey("AditionalList", on_delete=models.CASCADE)



class AditionalList(models.Model):
    adicional_id = models.ForeignKey("products.Aditional", on_delete=models.CASCADE)
