from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from authentication.models import Role
from core.models import Ticket

User = get_user_model()


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


def user_as_dict(user: User):
    return {
        "id": user.id,  # type: ignore
        "email": user.email,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "age": user.age,
        "phone": user.phone,
    }


def ticket_as_dict(ticket: Ticket):
    return {
        "id": ticket.id,  # type: ignore
        "operator": user_as_dict(ticket.operator),
        "resolved": ticket.resolved,
        "created_at": ticket.created_at,
        "updated_at": ticket.updated_at,
    }


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = User
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    operator = UserSerializer()
    client = UserSerializer()

    class Meta:
        model = Ticket
        fields = "__all__"


@api_view(["GET"])
def get_all_tickets(request):
    tickets = Ticket.objects.all()
    data = TicketSerializer(tickets, many=True).data
    return Response(data)
