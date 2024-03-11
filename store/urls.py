from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.ProductListAPIView.as_view()),
    path('product/<int:pk>/', views.ProductRetrieveAPIView.as_view()),
    path('product/<int:pk>/cartitem/',views.CartItemCreateAPIView.as_view()),
    path('product/<int:pk>/cartitem/<int:cartitem_id>/update/', views.CartItemUpdateAPIView.as_view()),
    path('product/<int:pk>/cartitem/<int:cartitem_id>/delete/', views.CartItemDestroyAPIView.as_view()),
    path('cart/<int:pk>/', views.CartAPIView.as_view()),
    path('order/<int:cart_id>/', views.OrderAPIView.as_view(), name='create_order'),

]