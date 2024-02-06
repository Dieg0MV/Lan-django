from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.

'Por ahora solo hace una peticion a esos datos devolviendolos en crudo'
def hello(request):
    #products = list(Product.objects.values())
    items = Product.objects.all()
    return render(request, 'index.html',{
        'items':items
    })

