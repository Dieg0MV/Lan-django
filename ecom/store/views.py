from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
# Create your views here.
def Home(request):
     return render(request, 'Home.html')

def items(request):
     return render(request, 'index.html')