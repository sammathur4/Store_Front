from django.db.models import Q, F
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import store.models
from django.db.models.aggregates import *

Product = store.models.Product
OrderItem = store.models.OrderItem
Order = store.models.Order


# Create your views here.


# def calculate():
#     x = 1
#     y = 2
#     return x

def say_hello(request):
    # query_set = Product.objects.filter(id__in = OrderItem.objects.values(
    #     'product_id').distinct()
    #                                    ).order_by('title')
    # query_set = OrderItem.objects.values('product_id').distinct()

    # query_set = Product.objects.only('id', 'title')
    # query_set = Product.objects.prefetch_related('promotions').select_related('collection').all()

    # query_set = Order.objects.select_related('customer').order_by('-placed_at')[:5]
    # query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    # result = Product.objects.aggregate(count=Count('id'),
    #                                    min_price = Min('price'))
    result = Product.objects.filter(collection__id = 1).aggregate(count=Count('id'))
    return render(request,
                  'hello.html',
                  {
                      'name': 'Sam',
                      'result': result,
                      # 'products': list(query_set)
                  }
                  )
