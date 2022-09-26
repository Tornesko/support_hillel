from django.core.exceptions import SuspiciousOperation
from django.db.models import Q
from rest_framework import generics
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from authentication.models import DEFAULT_ROLES
from core.models import Ticket
from core.permissions import ClientOnly, OperatorOnly
from core.serializers import TicketAssignSerializer, TicketSerializer
from core.services import TicketsCRUD


class ApiTicketsList(generics.ListCreateAPIView):
    """List all tickets, or create a new ticket."""

    def get_queryset(self):
        user = self.request.user
        if user.role.id == 1:
            return Ticket.objects.all()
        return Ticket.objects.filter(client=user)

    serializer_class = TicketSerializer
    permission_classes = (ClientOnly,)


class ApiTicket(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (ClientOnly,)
    serializer_class = TicketSerializer

    def retrieve(self, request, *args, **kwargs):
        ticket = Ticket.objects.get(pk=kwargs["pk"])
        serializer = TicketSerializer(ticket)

        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        empty = self.request.GET.get("empty", None)

        if user.role.id == DEFAULT_ROLES["admin"]:
            if empty == "true":
                return Ticket.objects.filter(operator=None)
            if empty == "false":
                return Ticket.objects.filter(operator=user)
            if empty is not None:
                raise SuspiciousOperation(
                    "Not allowed value. Only 'true' or 'false', only lowercase."
                )
            return Ticket.objects.filter(Q(operator=None) | Q(operator=user))

        if user.role.id == 1:
            return Ticket.objects.filter(operator=None) | Ticket.objects.filter(
                operator=user
            )
        if empty is not None:
            raise SuspiciousOperation("Not allowed. Operators only.")

        return Ticket.objects.filter(client=user)


class TicketAssignAPI(UpdateAPIView):
    http_method_names = ["patch"]
    serializer_class = TicketAssignSerializer
    permission_classes = [OperatorOnly]
    lookup_field = "id"
    lookup_url_kwarg = "id"

    def get_queryset(self):
        return Ticket.objects.filter(operator=None)


class TicketResolveAPI(UpdateAPIView):
    http_method_names = ["patch"]
    permission_classes = [OperatorOnly]
    serializer_class = TicketSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id"

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(operator=user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance = TicketsCRUD.change_resolved_status(instance)

        # serializer = self.serializer_class(instance)
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
