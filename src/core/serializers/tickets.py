from itertools import chain

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
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

    def validate(self, attrs: dict) -> dict:
        theme = attrs.get("theme")
        if not theme:
            return attrs

        data = Ticket.objects.values_list("theme")

        for element in chain.from_iterable(data):
            if element == theme:
                raise ValidationError("This ticket is already in the database")

        attrs["client"] = self.context["request"].user
        return attrs

    class Meta:
        model = Ticket
        fields = "__all__"


class TicketAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["operator"]

    def validate(self, attrs: dict) -> dict:
        # NOTE: Add current user to the `attrs` object
        attrs["operator"] = self.context["request"].user
        return attrs
