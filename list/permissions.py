from rest_framework import permissions
from .models import List, Item

class OwnerAwarePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, List) and obj.owner.id == request.user.id:
            return True

        if isinstance(obj, Item) and obj.list.owner.id == request.user.id:
            return True

        return False