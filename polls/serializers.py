from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from dynamic_rest.serializers import DynamicModelSerializer
from rest_framework import serializers
from dynamic_rest.serializers import DynamicModelSerializer


class UserSerializer(DynamicModelSerializer):

    class Meta:
        model = get_user_model()
        name = 'result'
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
