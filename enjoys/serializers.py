from rest_framework import serializers
from .models import EnjoyModel
from photos.serializers import ImageSerializer



class EnjoySerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True,many=True)
    class Meta:
        model = EnjoyModel
        fields = '__all__'