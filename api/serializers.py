from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Anfrage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AnfrageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Anfrage
        fields = ['unternehmen', 'kunden_email', 'text', 'start_datum', 'end_datum']
