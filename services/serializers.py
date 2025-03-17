from rest_framework import serializers
from .models import ServiceModel
from photos.serializers import ImageSerializer

class ServiceSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True,many=True)
    class Meta:
        model = ServiceModel
        fields = '__all__'