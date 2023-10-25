from django.db.models import Q, F
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import store.models
from django.db.models.aggregates import *
from django.db.models import *
from django.db.models.functions import *
from django.contrib.contenttypes.models import ContentType
import tags.models

Product = store.models.Product
OrderItem = store.models.OrderItem
Order = store.models.Order
Customer = store.models.Customer
TaggedItem = tags.models.TaggedItem

# Create your views here.


# def calculate():
#     x = 1
#     y = 2
#     return x




def say_hello(request):
    query_set = TaggedItem.objects.get_tags_for(Product, 1)
    return render(request,
                  'hello.html',
                  {
                      'name': 'Sam',
                      'result': query_set,
                      # 'products': list(query_set)
                  }
                  )
