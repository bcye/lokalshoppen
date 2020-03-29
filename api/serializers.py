from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Request, TimeSlot, Company, Category, SubCategory


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['start', 'end']


class AnfrageSerializer(serializers.ModelSerializer):
    slot = SlotSerializer()

    class Meta:
        model = Request
        fields = ['unternehmen_id', 'kunden_email', 'text', 'slot']

    def create(self, validated_data):
        slot_data = validated_data.pop('slot')
        slot = TimeSlot.objects.get(unternehmen=validated_data['unternehmen_id'], start=slot_data['start'], end=slot_data['end'])
        return Request.objects.create(slot=slot, **validated_data)


class UnternehmenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['email', 'name', 'adresse', 'point'
                  'telefon', 'max_pro_slot', 'oeffnungszeiten', 'beschreibung', 'ober_kategorien', 'unter_kategorien']


class OberKategorienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug', 'name']


class UnterKategorienSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['slug', 'name']
