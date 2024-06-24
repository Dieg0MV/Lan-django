from rest_framework import serializers
from .models import landis

class LandisSerializer(serializers.ModelSerializer):
  class Meta():
    model = landis
    
    filed = '__all__'