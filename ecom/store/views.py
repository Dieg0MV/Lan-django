from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.
def hello(request):
    return HttpResponse('Hello world')
#datos mostrados en formato json
def products(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)
