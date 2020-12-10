from rest_framework import serializers
from .models import Hero
class Heroserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        Model = Hero
        fields = ('name', 'alias')
