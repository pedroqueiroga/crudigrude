from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Departamento, Funcionario


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'url',
            'username',
            'email',
            'password',
            'groups',
            'funcionario',
        )
        read_only_fields = ['groups', 'funcionario']
        extra_kwargs = {
            'url': {'view_name': 'core:user-detail',},
            'groups': {'view_name': 'core:group-detail',},
            'funcionario': {'view_name': 'core:funcionario-detail',},
        }

    def validate_password(self, value):
        return make_password(value)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        extra_kwargs = {'url': {'view_name': 'core:group-detail'}}


class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = (
            'url',
            'nome',
            'funcao',
            'idade',
            'user',
            'departamento',
        )
        read_only_fields = ['user', 'departamento']
        extra_kwargs = {
            'url': {'view_name': 'core:funcionario-detail',},
            'departamento': {'view_name': 'core:departamento-detail',},
            'user': {'view_name': 'core:user-detail',},
        }


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = (
            'url',
            'nome',
        )
        extra_kwargs = {
            'url': {'view_name': 'core:departamento-detail',},
        }
