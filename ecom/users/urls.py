from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.cerrarsesion ),
    path('signup/', views.sing ),
    path('login/', views.signin )

]



