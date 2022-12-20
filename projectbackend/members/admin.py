from django.contrib import admin
from .models import Profile, Product, Post

admin.site.register(Profile)

admin.site.register(Post)



class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'price')
admin.site.register(Product, ProductAdmin)
