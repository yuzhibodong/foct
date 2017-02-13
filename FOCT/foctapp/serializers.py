from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import Collector,Foct
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('url','username','email')
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=('url','name')
class CollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Collector
        fields='__all__'


