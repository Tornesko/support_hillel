from rest_framework.permissions import BasePermission


class ClientOnly(BasePermission):
    message = "Not allowed. ClientOnly."

    def has_permission(self, request, view):
        if request.user.role.id == 2:
            return True

        return False
