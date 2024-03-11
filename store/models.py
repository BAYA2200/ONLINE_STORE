from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=1, max_digits=5)

    def __str__(self):
        return f"{self.name} {self.price}"


class Cart(models.Model):
    date_shopping_cart = models.DateTimeField(auto_now_add=True)
    all_price_product_cart = models.DecimalField(decimal_places=3, max_digits=10, default=0)

    def __str__(self):
        return f"{self.all_price_product_cart}"

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity_product = models.IntegerField(default=1)

    def __str__(self):
        return f"product {self.product} price {self.cart} quantity_product {self.quantity_product}"

class Order(models.Model):
    order_creation_date = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_cost_order = models.DecimalField(decimal_places=3, max_digits=10)
