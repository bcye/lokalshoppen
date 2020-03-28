from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AnfrageSerializer, UnternehmenSerializer, OberKategorienSerializer, UnterKategorienSerializer
from .models import Anfrage, Unternehmen, OberKategorie, UnterKategorie
from django.http import HttpResponse, HttpResponseForbidden


class AnfrageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows togoAnfragen to be viewed or edited.
    """
    queryset = Anfrage.objects.all()
    serializer_class = AnfrageSerializer
    http_method_names = ['post']


class UnternehmenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Unternehmen to be viewed or edited.
    """
    queryset = Unternehmen.objects.all()
    serializer_class = UnternehmenSerializer
    http_method_names = ['get', 'post']


class OberKategorienViewSet(viewsets.ModelViewSet):
    queryset = OberKategorie.objects.all()
    serializer_class = OberKategorienSerializer
    http_method_names = ['get']


class UnterKategorienViewSet(viewsets.ModelViewSet):
    queryset = UnterKategorie.objects.all()
    serializer_class = UnterKategorienSerializer
    http_method_names = ['get']


def confirm_purchase(request, id):
    if not request.user.is_authenticated or not  request.user.is_staff:
        return HttpResponseForbidden("Oops.")

    anfrage = Anfrage.objects.get(pk=id)
    anfrage.approved = True
    anfrage.save()

    return HttpResponse(content="Vielen Dank")