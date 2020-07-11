from django.contrib import admin

from .models import Category, Product, Photo, Cart, OrderStatus, Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(Cart)
admin.site.register(OrderStatus)
admin.site.register(Order)