from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Shipping)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)