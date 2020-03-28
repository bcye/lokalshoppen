# cookbook/ingredients/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import Anfrage, UnterKategorie, OberKategorie, Unternehmen, TimeSlot
import graphql_geojson

class AnfrageType(DjangoObjectType):
    class Meta:
        model = Anfrage

class OberKategorieType(DjangoObjectType):
    class Meta:
        model = OberKategorie

class UnterKategorieType(DjangoObjectType):
    class Meta:
        model = UnterKategorie

class TimeSlotType(DjangoObjectType):
    class Meta:
        model = TimeSlot


class UnternehmenType(graphql_geojson.GeoJSONType):
    class Meta:
        model = Unternehmen
        geojson_field = 'point'

class Query(object):
    alle_oberkategorien = graphene.List(OberKategorieType)
    alle_unterkategorien = graphene.List(UnterKategorieType)
    alle_unternehmen = graphene.List(UnternehmenType)
    alle_anfragen = graphene.List(AnfrageType)


    def resolve_alle_oberkategorien(self, info, **kwargs):
        return OberKategorie.objects.all()

    def resolve_alle_unterkategorien(self, info, **kwargs):
        return UnterKategorie.objects.all()

    def resolve_alle_anfragen(self, info, **kwargs):
        return Anfrage.objects.all()

    def resolve_alle_unternehmen(self, info, **kwargs):
        return Unternehmen.objects.all()


