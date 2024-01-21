from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
# Create your views here.
def hello(request):
    return HttpResponse('Hello world')

def products(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)
