from rest_framework import viewsets
from .serializers import AnfrageSerializer, UnternehmenSerializer, OberKategorienSerializer, UnterKategorienSerializer
from .models import Request, Company, Category, SubCategory
from django.http import HttpResponse, HttpResponseForbidden


class AnfrageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows togoAnfragen to be viewed or edited.
    """
    queryset = Request.objects.all()
    serializer_class = AnfrageSerializer
    http_method_names = ['post']


class UnternehmenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Unternehmen to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = UnternehmenSerializer
    http_method_names = ['get', 'post']


class OberKategorienViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = OberKategorienSerializer
    http_method_names = ['get']


class UnterKategorienViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = UnterKategorienSerializer
    http_method_names = ['get']


def confirm_purchase(request, id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("Oops.")

    anfrage = Request.objects.get(pk=id)
    anfrage.approved = True
    anfrage.save()

    return HttpResponse(content="Vielen Dank")
