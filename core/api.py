from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from core.models import Ticket
from core.serializers import TicketSerializer


class ApiTicketsList(generics.ListCreateAPIView):
    """List all tickets, or create a new ticket."""

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ApiTicket(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = TicketSerializer

    def retrieve(self, request, *args, **kwargs):
        ticket = Ticket.objects.get(pk=kwargs["pk"])
        serializer = TicketSerializer(ticket)

        return Response(serializer.data)
