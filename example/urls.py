from django.urls import path, include
from example import views
from example.views import CategoryCRUDView, ProductCRUDView

urlpatterns = [
    path('categories/<int:pk>/', CategoryCRUDView.as_view(), name='category-crud'),
    path('products/<int:pk>/', ProductCRUDView.as_view(), name='product-crud'),
]