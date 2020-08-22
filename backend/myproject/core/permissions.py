from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Makes sure that a user can only update his own data"""

    def has_object_permission(self, request, view, obj):
        if (
            request.method in permissions.SAFE_METHODS
        ) or request.user.is_staff:
            return True
        return request.user == obj.user


class CreateUserPermissions(permissions.BasePermission):
    """Users can only be created by admin or unauthenticated users"""

    def has_permission(self, request, view):
        if view.action == 'create':
            return (not request.user.is_authenticated) or request.user.is_staff
        return True


class ListForAdminsOnly(permissions.BasePermission):
    """Lists only allowed for admin"""

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user and request.user.is_staff
        return True


class IsSelfOrAdmin(permissions.BasePermission):
    """Allows self or staff."""

    def has_object_permission(self, request, view, obj):
        return (
            request.user
            and request.user.is_authenticated
            and (request.user.is_staff or request.user == obj)
        )
