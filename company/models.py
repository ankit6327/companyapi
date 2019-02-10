from django.db import models
from django.contrib.auth.models import User
from datetime import datetime   

class Companies(models.Model):
    companyName = models.CharField(max_length= 100, null="False")
    companyAddress = models.CharField(max_length=255, null=False)

    def __str__(self):
        return"{} - {}".format(self.companyName, self.companyAddress)


class Company(models.Model):
    name = models.CharField(max_length=200, null="False")
    active = models.BooleanField(default="True")
    dbName = models.CharField(max_length=200, null="True")

    def __self__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, null="True")

    def __self__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null="False")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __self__(self):
        return self.name

class Order(models.Model):
    status = models.BooleanField(default="True")
    createdDate = models.DateTimeField(default=datetime.now, blank=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __self__(self):
        return self.status

class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __self__(self):
        return self



