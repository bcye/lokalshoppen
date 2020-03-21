from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, AnfrageSerializer, UnternehmensProfilSerializer
from .models import Anfrage, UnternehmensProfil


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


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
