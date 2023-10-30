from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import *
from rest_framework import *
from rest_framework import status
from rest_framework.decorators import *
from rest_framework.response import *
from rest_framework.filters import  SearchFilter
from .filters import ProductFilter
from .models import *
from .serializers import *
from rest_framework.views import *
from rest_framework.mixins import *
from rest_framework.generics import *
from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['collection_id', 'unit_price']
    filterset_class = ProductFilter
    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     collection_id = self.request.query_params.get('collection_id')
    #     if collection_id is not None:
    #         queryset = queryset.filter(collection_id=collection_id)
    #
    #     return queryset

    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_class = ProductFilter
    # pagination_class = DefaultPagination
    # permission_classes = [IsAdminOrReadOnly]
    # search_fields = ['title', 'description']
    # ordering_fields = ['unit_price', 'last_update']

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('product')).all()
    serializer_class = CollectionsSerializer

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']):
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_pk']
        return Review.objects.filter(product_id=product_id)


    def get_serializer_context(self):
        print("self.kwargs['product_pk']", self.kwargs['product_pk'])
        return {'product_id': self.kwargs['product_pk']}