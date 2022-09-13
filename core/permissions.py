from rest_framework.permissions import BasePermission

from authentication.models import DEFAULT_ROLES


class ClientOnly(BasePermission):
    message = "Not allowed. ClientOnly."

    def has_permission(self, request, view):
        if request.user.role.id == 2:
            return True

        return False


class OperatorOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.role.id == DEFAULT_ROLES["admin"]:
            return True

        return False