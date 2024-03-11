from django.contrib import admin

# Register your models here.
from store.models import Product, Cart, CartItem, Order

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)


