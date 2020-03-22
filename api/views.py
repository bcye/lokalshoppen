from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AnfrageSerializer, UnternehmensProfilSerializer
from .models import Anfrage, UnternehmensProfil
from django.http import HttpResponse, HttpResponseForbidden


class AnfrageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows togoAnfragen to be viewed or edited.
    """
    queryset = Anfrage.objects.all()
    serializer_class = AnfrageSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class UnternehmenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Unternehmen to be viewed or edited.
    """
    queryset = UnternehmensProfil.objects.all()
    serializer_class = UnternehmensProfilSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


def confirm_purchase(request, id):
    if not request.user.is_authenticated or not  request.user.is_staff:
        return HttpResponseForbidden("Oops.")

    anfrage = Anfrage.objects.get(id)
    anfrage.approved = True
    anfrage.save()

    return HttpResponse(content="Vielen Dank")