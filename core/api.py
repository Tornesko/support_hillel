from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Ticket
from core.serializers import TicketLightSerializer, TicketSerializer


# @api_view(["GET", "POST"])
# def get_post_tickets(request):
#     if request.method == "GET":
#         tickets = Ticket.objects.all()
#         serializer = TicketLightSerializer(tickets, many=True).data
#         return Response(data=serializer)
#
#     serializer = TicketSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     instance = serializer.create(serializer.validated_data)
#     results = TicketSerializer(instance).data
#
#     return Response(data=results, status=status.HTTP_201_CREATED)

class ApiTicketsList(APIView):
    """List all tickets, or create a new ticket."""

    def get(self, request, format=None):
        tickets = Ticket.objects.all()
        serializer = TicketLightSerializer(tickets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def get_ticket(request, id_):
#     if request.method == "GET":
#         tickets = Ticket.objects.get(id=id_)
#         serializer = TicketSerializer(tickets).data
#         return Response(data=serializer)
#     if request.method == "DELETE":
#         ticket = Ticket.objects.get(id=id_)
#         ticket.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ApiTicket(APIView):

    def get(self, request, id_):
        ticket = Ticket.objects.get(id=id_)
        serializer = TicketSerializer(ticket).data
        return Response(data=serializer)

    def put(self, request, id_):
        ticket = Ticket.objects.get(id=id_)
        serializer = TicketSerializer(ticket).data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_):
        ticket = Ticket.objects.get(id=id_)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
