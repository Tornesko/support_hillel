from rest_framework.permissions import BasePermission

from authentication.models import DEFAULT_ROLES
from core.models import Ticket


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


class IsAuthenticatedAndOwner(BasePermission):
    message = "You must be admin or authenticated."

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class CommentViewPermission(BasePermission):
    def has_permission(self, request, view):
        ticket_id = view.kwargs.get("ticket_id")
        ticket = Ticket.objects.get(id=ticket_id)
        user = request.user

        if user.role.id == DEFAULT_ROLES["admin"] and ticket.operator.id == user.id:
            return True
        return False


class CommentCreatePermission(BasePermission):
    def has_permission(self, request, view):
        ticket_id = view.kwargs.get("ticket_id")
        ticket = Ticket.objects.get(id=ticket_id)

        if ticket.operator is None:
            return False
        if ticket.status == "resolved":
            return False
        return True
