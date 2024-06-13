from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        author = (
            obj.author
            if request.method in ['PUT', 'DELETE']
            else obj['author']
        )
        return (
            request.method in SAFE_METHODS
            or author == request.user
        )
