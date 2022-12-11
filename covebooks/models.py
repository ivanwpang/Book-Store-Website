from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Order(models.Model):
    #customer = models.ForiegnKey(Profile, on_delete=models.SET_NULL, null=true, blank=true)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class Shipping(models.Model):
    firstname = models.CharField(max_length=255, default="", null=True)
    lastname = models.CharField(max_length=255, default="", null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    phoneNumber = models.CharField(max_length=10, default="", blank=True, null=True)
    address = models.CharField(max_length=255, default="", null=True)
    city = models.CharField(max_length=255, default="", null=True)
    state = models.CharField(max_length=2, default="", null=True)
    zipCode = models.CharField(max_length=5, default="", null=True) 
    instructions = models.TextField(max_length=255, default="", blank=True, null=True)
    #date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lastname + " " + self.firstname

class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    #image
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
