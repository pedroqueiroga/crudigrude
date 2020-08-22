from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .models import Departamento, Funcionario
from .serializers import (DepartamentoSerializer, FuncionarioSerializer,
                          GroupSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    '''
    This viewset automatically provides `list` and `detail` actions for users.
    '''

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    '''
    This viewset automatically provides `list` and `detail` actions for groups.
    '''

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class FuncionarioViewSet(viewsets.ModelViewSet):
    '''
    This viewset automtically provides `list` and `detail` actions for funcionarios.
    '''

    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartamentoViewSet(viewsets.ModelViewSet):
    '''
    This viewset automtically provides `list` and `detail` actions for departamentos.
    '''

    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
