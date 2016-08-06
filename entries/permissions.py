from rest_framework import permissions

class IsAuthorOfPost(permissions.BasePermission):
    def has_object_permission(self, request, view, entry):
        if request.user:
            return entry.author == request.user
        return False