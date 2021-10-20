from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    # Make sure that only the author of a review is manipulating and others can read
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
