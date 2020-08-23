from django.contrib.auth.models import Group, User
from rest_framework import mixins, permissions, viewsets

from .models import Departamento, Funcionario
from .permissions import (CreateUserPermissions, IsAdminOrReadOnly,
                          IsOwnerOrReadOnly, IsSelfOrAdmin, ListForAdminsOnly)
from .serializers import (DepartamentoSerializer, FuncionarioSerializer,
                          GroupSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    '''
    This viewset provides `list`, `detail`, `update`, `delete`, `create` actions for users.
    '''

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [
    #     CreateUserPermissions,
    #     ListForAdminsOnly,
    #     IsSelfOrAdmin,
    # ]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This viewset provides `list` and `detail` actions for groups.
    '''

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None


class FuncionarioViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    '''
    This viewset provides `list`, `detail` and `update` actions for funcionarios.
    '''

    queryset = Funcionario.objects.all().order_by('-id')
    serializer_class = FuncionarioSerializer
    permission_classes = [permissions.AllowAny]
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsOwnerOrReadOnly,
    # ]

    def get_queryset(self):
        queryset = super(FuncionarioViewSet, self).get_queryset()
        order_by = self.request.query_params.get('orderby', '')
        if order_by:
            try:
                # categories and directions
                order_by_cat, order_by_dir, *_ = [*order_by.split(','), '']
                order_by_sign = '-' if order_by_dir == 'desc' else ''
                queryset = queryset.order_by(
                    ''.join([order_by_sign, order_by_cat])
                )
            except:
                pass
        return queryset


class DepartamentoViewSet(viewsets.ModelViewSet):
    '''
    This viewset provides `list`, `detail`, `update`, `delete`, `create` actions for users.
    '''

    queryset = Departamento.objects.all().order_by('-nome')
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
