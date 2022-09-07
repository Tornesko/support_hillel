from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import Ticket
from core.serializers import TicketSerializer


class ApiTicketsList(generics.ListCreateAPIView):
    """List all tickets, or create a new ticket."""

    def get_queryset(self):
        user = self.request.user
        if user.role.id == 1:
            return Ticket.objects.all()
        return Ticket.objects.filter(client=user)

    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)


class ApiTicket(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer

    def retrieve(self, request, *args, **kwargs):
        ticket = Ticket.objects.get(pk=kwargs["pk"])
        serializer = TicketSerializer(ticket)

        return Response(serializer.data)
