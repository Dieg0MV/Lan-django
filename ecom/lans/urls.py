from django.urls import path, include
from rest_framework import routers 
from . import views

router = routers.DefaultRouter()
router.register(r'Lans', views.LandsView, 'Lans')


urlpatterns = [
    path('api/Lans', include(router.urls))   
]
