from django.db.models import Q, F
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import store.models

Product = store.models.Product


# Create your views here.


# def calculate():
#     x = 1
#     y = 2
#     return x

def say_hello(request):
    # query_set = Product.objects.filter(inventory__lt=10).filter(price__gt=10)
    # query_set = Product.objects.filter(title__icontains = 'coffee')
    # query_set = Product.objects.filter(Q(inventory__lt =10) | Q(price__lt=20))
    # query_set = Product.objects.order_by('price','-title')
    query_set = Product.objects.all()
    #
    return render(request,
                  'hello.html',
                  {
                      'name':'Sam',
                      'products': list(query_set)
                   }
                  )