from django.shortcuts import render, get_object_or_404
from django.http import *
from rest_framework import *
from rest_framework import status
from rest_framework.decorators import *
from rest_framework.response import *
from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        return Response('ok')


@api_view()
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)




@api_view()
def collections_details(request, pk):
    return Response('ok')
