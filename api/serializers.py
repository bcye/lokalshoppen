from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Anfrage, TimeSlot


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# class AnfrageSerializer(serializers.Serializer):
#     unternehmen_id = serializers.IntegerField()
#     kunden_email = serializers.EmailField()
#     text = serializers.CharField()
#     slot = serializers.DictField(child=serializers.DateTimeField)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Anfrage` instance, given the validated data.
#         """
#         slot = TimeSlot.objects.create(start=validated_data['slot']['start_datum'], end=validated_data['slot']['end_datum'])
#         return Anfrage.objects.create(
#             unternehmen=User.objects.get(validated_data['unternehmen_id']),
#             kunden_email=validated_data['kunden_email'],
#             text=validated_data['text'],
#             slot=slot
#         )


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
