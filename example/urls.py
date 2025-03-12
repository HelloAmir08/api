from django.urls import path, include
from example import views
from example.views import ProductList, ProductDetail

urlpatterns = [
    path('product-list/', ProductList.as_view(), name='product-list'),
    path('product-detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]