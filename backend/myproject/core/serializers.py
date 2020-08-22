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
            'groups',
        )
        extra_kwargs = {
            'url': {'view_name': 'core:user-detail',},
            'groups': {'view_name': 'core:group-detail',},
        }

    def create(self, validated_data):
        """Creates an empty Funcionario associated with this user."""
        user = User.objects.create(
            email=validated_data['email'], username=validated_data['username'],
        )
        user.groups.set(validated_data['groups'])
        try:
            funcionario = Funcionario.objects.create(
                nome="", user=user, funcao=""
            )
        except Exception as e:
            user.delete()
            raise e

        return user


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
        read_only_fields = ['user']
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
