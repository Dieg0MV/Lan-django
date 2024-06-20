from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home),
    path('lans/', views.items, name='lans')   
]
