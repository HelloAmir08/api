from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from example.models import Product
from example.serializers import ProductModelSerializer


# Create your views here.

class ProductList(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serializers = ProductModelSerializer(products, many=True)

        return Response(serializers.data)

class ProductDetail(APIView):

    def get(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        serializers = ProductModelSerializer(product)

        return Response(serializers.data)

