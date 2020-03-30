# cookbook/ingredients/schema.py
import graphene
from .models import Request, SubCategory, Category, Company, TimeSlot

import graphql_geojson
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_geojson.filters import GeometryFilterSet, DistanceFilter
from graphql_geojson.fields import DistanceField
from django.contrib.gis import forms
from graphene_django.forms.converter import convert_form_field

# Filters
class CompanyFilter(GeometryFilterSet):
    class Meta:
        model = Company
        fields = {
            'name': ['exact'],
            'location': ['exact', 'intersects'],
            "active": ['exact']
        }

# Node types
class RequestNode(DjangoObjectType):
    class Meta:
        model = Request
        interfaces = (relay.Node, )


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (relay.Node, )

        filter_fields = ["name", "slug"]


class SubCategoryNode(DjangoObjectType):
    class Meta:
        model = SubCategory
        interfaces = (relay.Node, )

        filter_fields = ["name", "slug"]


class TimeSlotNode(DjangoObjectType):
    class Meta:
        model = TimeSlot
        interfaces = (relay.Node, )
        filter_fields = ["start", "end"]



class CompanyNode(graphql_geojson.GeoJSONType):
    class Meta:
        model = Company
        geojson_field = 'location'

        interfaces = (relay.Node, )

class Query(object):
    all_categories = DjangoFilterConnectionField(CategoryNode)
    all_sub_categories = DjangoFilterConnectionField(SubCategoryNode)
    all_companies = DjangoFilterConnectionField(CompanyNode, filterset_class=CompanyFilter)


