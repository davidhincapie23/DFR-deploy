from rest_framework import serializers
from .models import Desarrollador

class Desarrolladorserializers (serializers.ModelSerializer):
    class Meta:
        model = Desarrollador
        fields = '__all__'



