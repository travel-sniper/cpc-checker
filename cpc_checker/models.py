from django.db import models


class Result(models.Model):
    url = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    price_inc_vat = models.CharField(max_length=10)
    product_no = models.CharField(max_length=10)
    order_code = models.CharField(max_length=10)
    in_stock = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date
