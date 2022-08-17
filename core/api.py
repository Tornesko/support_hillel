from rest_framework import generics

from core.models import Ticket
from core.serializers import TicketLightSerializer, TicketSerializer


class ApiTicketsList(generics.ListCreateAPIView):
    """List all tickets, or create a new ticket."""
    queryset = Ticket.objects.all()
    serializer_class = TicketLightSerializer


class ApiTicket(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
