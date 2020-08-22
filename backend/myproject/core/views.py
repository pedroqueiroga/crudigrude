from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer


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
