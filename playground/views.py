from django.db.models import Q, F
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import store.models
from django.db.models.aggregates import *
from django.db.models import *
from django.db.models.functions import *

Product = store.models.Product
OrderItem = store.models.OrderItem
Order = store.models.Order
Customer = store.models.Customer


# Create your views here.


# def calculate():
#     x = 1
#     y = 2
#     return x

def say_hello(request):
    # query_set = Customer.objects.annotate(is_new=Value(True))
    query_set = Customer.objects.annotate(
        full_name=Func(F('first_name'),Value(' '),F('last_name'), function='CONCAT')
    )

    query_set = Customer.objects.annotate(
        full_name=Concat('first_name', Value(' '), 'last_name')
    )

    return render(request,
                  'hello.html',
                  {
                      'name': 'Sam',
                      'result': query_set,
                      # 'products': list(query_set)
                  }
                  )
