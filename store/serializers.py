from rest_framework import serializers
from store.models import Product, Cart, CartItem, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    cartitem_set = CartItemSerializer(many=True, read_only=True)
    all_price_product_cart = serializers.SerializerMethodField()

    # cart = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

    def get_all_price_product_cart(self, obj):
        # Вычисляем общую стоимость всех товаров в корзине
        total_price = sum(item.product.price * item.quantity_product for item in obj.cartitem_set.all())
        return total_price


class CartItemSerializer2(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ['product', 'cart']


class OrderSerializer(serializers.ModelSerializer):
    total_cost_order = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_total_cost_order(self, obj):
        # Вычисляем общую стоимость заказа на основе данных из связанных товаров в корзине
        total_cost_order = sum(item.product.price * item.quantity_product for item in obj.cart.cartitem_set.all())
        return total_cost_order