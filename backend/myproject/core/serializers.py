from django.contrib.auth.models import Group, User
from rest_framework import serializers


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


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        extra_kwargs = {'url': {'view_name': 'core:group-detail'}}
