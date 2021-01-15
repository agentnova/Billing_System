from django.db import models


class ProductModel(models.Model):
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


class PurchaseModel(models.Model):
    product_name = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    buying_price = models.IntegerField(default=1)
    selling_price = models.IntegerField(default=10)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.product_name)


class SalesModel(models.Model):
    bill_number = models.CharField(unique=True, max_length=100)
    customer_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    bill_total = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.bill_number


class OrderModel(models.Model):
    bill_number = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField(default=0)
