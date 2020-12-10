from django.shortcuts import render
from .models import Hero
from .serializers import Heroserializers
from rest_framework import viewsets
# Create your views here.
class heroviewsets(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = Heroserializers
