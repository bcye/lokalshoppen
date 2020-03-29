# cookbook/ingredients/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import Request, SubCategory, Category, Company, TimeSlot
import graphql_geojson

class RequestType(DjangoObjectType):
    class Meta:
        model = Request

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class SubCategory(DjangoObjectType):
    class Meta:
        model = SubCategory

class TimeSlotType(DjangoObjectType):
    class Meta:
        model = TimeSlot


class CompanyType(graphql_geojson.GeoJSONType):
    class Meta:
        model = Company
        geojson_field = 'location'

class Query(object):
    all_categories = graphene.List(CategoryType)
    all_sub_categories = graphene.List(SubCategory)
    all_companies = graphene.List(CompanyType)
    all_requests = graphene.List(RequestType)


    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_sub_categories(self, info, **kwargs):
        return SubCategory.objects.all()

    def resolve_all_requests(self, info, **kwargs):
        return Request.objects.all()

    def resolve_all_companies(self, info, **kwargs):
        return Company.objects.all()


