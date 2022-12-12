from django.contrib import admin
from .models import *
from members.models import Profile

admin.site.register(Shipping)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)