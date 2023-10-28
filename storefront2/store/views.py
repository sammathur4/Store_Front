from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import *
from rest_framework import *
from rest_framework import status
from rest_framework.decorators import *
from rest_framework.response import *
from .models import *
from .serializers import *
from rest_framework.views import *
from rest_framework.mixins import *
from rest_framework.generics import *
from rest_framework.viewsets import ModelViewSet


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.orderitems.count() > 0:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item.'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('product')).all()
    serializer_class = CollectionsSerializer

    def delete(self, request,pk):
        collection = get_object_or_404(
            Collection.objects.annotate(
                products_count=Count('product')), pk=pk)

        if collection.product_set.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

