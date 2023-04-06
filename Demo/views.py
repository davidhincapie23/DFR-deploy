from django.shortcuts import render
from rest_framework import viewsets
from .models import Desarrollador
from .serializers import Desarrolladorserializers
# Create your views here.


class DesarrolladorViewSet(viewsets.ModelViewSet):
    serializer_class = Desarrolladorserializers
    queryset = Desarrollador.objects.all()