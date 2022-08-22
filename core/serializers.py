from django.contrib.auth import get_user_model
from rest_framework import serializers

from authentication.models import Role
from core.models import Ticket

User = get_user_model()


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("name",)


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = User
        fields = ("role", "email", "username", "first_name", "last_name", "phone")


class UserLightSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = User
        fields = ("role", "username")


# class TicketLightSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ticket
#         fields = ('operator', 'client', 'theme', 'resolved')


class TicketSerializer(serializers.ModelSerializer):
    client = serializers.HiddenField(default=serializers.CurrentUserDefault())
    operator = UserLightSerializer()

    class Meta:
        model = Ticket
        fields = "__all__"


# class CreateTicketSerializer(serializers.ModelSerializer):
#     client = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     operator = UserSerializer()
#
#     class Meta:
#         model = Ticket
#         fields = "__all__"
