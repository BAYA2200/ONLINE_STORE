
from rest_framework import generics, status
from decimal import Decimal

# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Product, Cart, CartItem, Order
from store.serializers import ProductSerializer, CartSerializer, CartItemSerializer, CartItemSerializer2, \
    OrderSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartItemCreateAPIView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        product_id = self.kwargs.get('pk')
        product = get_object_or_404(Product, id=product_id)
        serializer.save(product=product)


class CartItemUpdateAPIView(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer2


class CartItemDestroyAPIView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartAPIView(APIView):
    def get(self, request, pk):
        cart = get_object_or_404(Cart, pk=pk)
        serializers = CartSerializer(cart)
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class OrderAPIView(APIView):
    def post(self, request, cart_id):
        cart = get_object_or_404(Cart, pk=cart_id)

        # Вычисляем общую стоимость заказа на основе данных из корзины
        total_cost_order = sum(Decimal(item.product.price) * item.quantity_product for item in cart.cartitem_set.all())

        # Создаем объект заказа
        order = Order.objects.create(cart=cart, total_cost_order=total_cost_order)

        # Возвращаем данные заказа в ответе
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, cart_id):
        cart = get_object_or_404(Cart, pk=cart_id)

        # Удаляем все товары из корзины
        cart.cartitem_set.all().delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
