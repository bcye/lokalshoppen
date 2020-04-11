# cookbook/ingredients/schema.py
import graphene
from .models import Request, SubCategory, Category, Company, TimeSlot, BusinessHours

import graphql_geojson
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_geojson.filters import GeometryFilterSet, DistanceFilter
from graphql_geojson.fields import DistanceField
from django.contrib.gis import forms
from graphene_django.forms.converter import convert_form_field
from django.db.models import Prefetch, Count, F
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphql_relay import from_global_id
from django.utils import timezone

# Filters
class CompanyFilter(GeometryFilterSet):
    class Meta:
        model = Company
        fields = {
            'name': ['exact'],
            'location': ['exact', 'intersects'],
            "active": ['exact'],
            "category": ["exact"],
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

class BusinessHoursNode(DjangoObjectType):
    class Meta:
        model = BusinessHours
        interfaces = (relay.Node, )


class TimeSlotNode(DjangoObjectType):
    available = graphene.Boolean()

    def resolve_available(parent, info):
        if hasattr(parent, "available"):
            return parent.available > 0
        else:
            return parent.check_available()

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.filter(start__gte=timezone.now())

    class Meta:
        model = TimeSlot
        interfaces = (relay.Node, )
        filter_fields = ["start", "end"]


class CompanyNode(graphql_geojson.GeoJSONType):
    class Meta:
        model = Company
        geojson_field = 'location'

        interfaces = (relay.Node, )

# Filtered company queryset used by GraphQL endpoints
def get_company_queryset(start):
    return Company.objects.all().prefetch_related(
            Prefetch(
                "timeslot_set",
                queryset=TimeSlot.objects.annotate(available=F("company__max_per_slot")-Count("request")).filter(start__gte=timezone.now(start))
            )).filter(
                active=True,
            )

class Query(object):
    all_categories = DjangoFilterConnectionField(CategoryNode)
    all_sub_categories = DjangoFilterConnectionField(SubCategoryNode)
    all_companies = DjangoFilterConnectionField(CompanyNode, filterset_class=CompanyFilter)

    company = relay.Node.Field(CompanyNode)

    def resolve_all_companies(self, info, **kwargs):
        d = timezone.now()
        return get_company_queryset(d)


class CreateRequest(relay.ClientIDMutation):
    class Input:
        company_id = graphene.ID(required=True)
        slot_id = graphene.ID(required=True)
        customer_email = graphene.String(required=True)
        text = graphene.String(required=True)

    data = graphene.Field(RequestNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        request = Request()
        request.text = input["text"]    
        request.customer_email = input["customer_email"]
        request.company_id = from_global_id(input["company_id"])[1]
        request.slot_id = from_global_id(input["slot_id"])[1]

        request.save()
        return CreateRequest(data=request)

class BusinessHoursInput(graphene.InputObjectType):
    start = graphene.Time()
    end = graphene.Time()
    weekday = graphene.Enum("WeekdayType", [(label, key) for key, label in BusinessHours.WEEKDAYS])()


class CreateCompany(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        address = graphene.String(required=True)
        email = graphene.String(required=True)
        description = graphene.String(required=True)
        location = graphql_geojson.Geometry(required=True)
        category_id = graphene.ID(required=True)
        sub_category_ids = graphene.List(graphene.ID)
        phone = graphene.String()
        max_per_slot = graphene.Int()
        business_hours_set = graphene.List(BusinessHoursInput)


    data = graphene.Field(CompanyNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        sub_categories = [from_global_id(x)[1] for x in input.pop("sub_category_ids", [])]
        business_hours = input.pop("business_hours_set", [])
        input["category_id"] = from_global_id(input["category_id"])[1]
        company = Company.objects.create(**input)
        company.sub_categories.set(sub_categories)

        for bhdata in business_hours:
            company.businesshours_set.create(**bhdata)
        
        return CreateRequest(data=company)

class Mutations(graphene.ObjectType):
    createRequest = CreateRequest.Field()
    createCompany = CreateCompany.Field()

