from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Anfrage, TimeSlot, Unternehmen


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['start', 'end']


class AnfrageSerializer(serializers.ModelSerializer):
    slot = SlotSerializer()

    class Meta:
        model = Anfrage
        fields = ['unternehmen_id', 'kunden_email', 'text', 'slot']

    def create(self, validated_data):
        slot_data = validated_data.pop('slot')
        slot = TimeSlot.objects.get(unternehmen=validated_data['unternehmen_id'], start=slot_data['start'], end=slot_data['end'])
        return Anfrage.objects.create(slot=slot, **validated_data)


class UnternehmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unternehmen
        fields = ['email', 'name', 'adresse', 'point'
                  'telefon', 'max_pro_slot', 'oeffnungszeiten', 'beschreibung', 'ober_kategorie', 'unter_kategorien']