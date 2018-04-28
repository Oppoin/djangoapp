from django.contrib.auth.models import User, Group
from rest_framework import serializers
from dynamic_rest.serializers import DynamicModelSerializer


#class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(DynamicModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
