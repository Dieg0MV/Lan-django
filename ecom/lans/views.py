from rest_framework import viewsets
from .serializer import LandisSerializer
from .models import landis
# Create your views here.


class LandsView(viewsets.ModelViewSet):
     serializer_class =  LandisSerializer
     queryset = landis.objects.all() 
     