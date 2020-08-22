from django.contrib.auth.models import Group, User
from rest_framework import mixins, permissions, viewsets

from .models import Departamento, Funcionario
from .serializers import (DepartamentoSerializer, FuncionarioSerializer,
                          GroupSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    '''
    This viewset provides `list`, `detail`, `update`, `delete`, `create` actions for users.
    '''

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This viewset provides `list` and `detail` actions for groups.
    '''

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class FuncionarioViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    '''
    This viewset provides `list`, `detail` and `update` actions for funcionarios.
    '''

    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartamentoViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This viewset automtically provides `list` and `detail` actions for departamentos.
    '''

    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
