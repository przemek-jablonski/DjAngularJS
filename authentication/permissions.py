from rest_framework import permissions

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, user_account):
        if request.user:
            return user_account == request.user
        return False