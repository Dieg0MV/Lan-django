from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def login():
    return HttpResponse('login')

def sing():
    return HttpResponse('sing up')
