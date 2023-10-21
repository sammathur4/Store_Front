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
    # x = calculate()
    # product = Product.objects.filter(pk = 0).first()
    # try:
    #     query_set = Product.objects.get(pk = 1)
    #     query_set.filter().filter().order_by()
    # except ObjectDoesNotExist:
    #     pass

    # prodcut = Product.objects.filter(pk=0).exist()

    # query_set = Product.objects.all()
    # query_set = Product.objects.filter(price__gt=20)
    # query_set = Product.objects.filter(price__range=(20,30))
    query_set = Product.objects.filter(title__icontains = 'coffee')
    # for product in query_set:
    #     print(product)



    return render(request,
                  'hello.html',
                  {
                      'name':'Sam',
                      'products': list(query_set)
                   }
                  )