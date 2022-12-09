from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Shipping(models.Model):
  firstname = models.CharField(max_length=255, default="")
  lastname = models.CharField(max_length=255, default="")
  phoneNumber = models.CharField(max_length=10, default="", blank=True)
  address = models.CharField(max_length=255, default="")
  city = models.CharField(max_length=255, default="")
  state = models.CharField(max_length=2, default="")
  zipCode = models.CharField(max_length=5, default="") 
  instructions = models.TextField(max_length=255, default="", blank=True)