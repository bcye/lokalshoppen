from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Anfrage, TimeSlot, UnternehmensProfil


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'


class AnfrageSerializer(serializers.ModelSerializer):
    slot = SlotSerializer()

    class Meta:
        model = Anfrage
        fields = '__all__'

    def create(self, validated_data):
        slot_data = validated_data.pop('slot')
        slot = TimeSlot.objects.create(**slot_data)
        return Anfrage.objects.create(slot=slot, **validated_data)


class UnternehmensProfilSerializer(serializers.ModelSerializer):
    # user = UnternehmenSerializer()

    class Meta:
        model = UnternehmensProfil
        fields = '__all__'
        depth = 1