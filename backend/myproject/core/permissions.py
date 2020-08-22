from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Makes sure that a user can only update his own data"""

    def has_object_permission(self, request, view, obj):
        if (
            request.method in permissions.SAFE_METHODS
        ) or request.user.is_staff:
            return True
        return request.user == obj.user


class CustomUserPermission(permissions.BasePermission):
    """Makes it so that unauthenticated users can only create users 
    and only staff can check out the list of users"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return request.method == 'POST'
        return request.user.is_staff


class IsSelfOrAdmin(permissions.BasePermission):
    """Allows self or staff."""

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user == obj
