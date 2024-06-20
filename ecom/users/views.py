from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.db import IntegrityError

def cerrarsesion(request):
    logout(request)
    return redirect('/')

def sing(request):
    if request.method == "GET":
        return render(request, 'sing-up.html',{
        "form": UserCreationForm
    })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], 
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("/items")
            
            except IntegrityError:
                 return render(request, 'sing-up.html',{
                    "form": UserCreationForm,
                    "error":'user alredy exist'
                    })      
        return render(request, 'sing-up.html',{
        "form": UserCreationForm,
        "error":'password do not match'
        })

def signin(request):
   if request.method == 'GET':
        return render(request,'logout.html',{
        'form':AuthenticationForm})
   else:
        user = authenticate(request,
                            username=request.POST["username"], 
                            password=request.POST['password'])
        if user is None:
            return render(request,'logout.html',{
        'form':AuthenticationForm,
        'error':'usuario o contraseña no validos'}) 
               
        else:
            login(request, user)
            return redirect('lans')