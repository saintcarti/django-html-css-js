from rest_framework import serializers
from .models import Camara

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camara
        fields = '__all__'
