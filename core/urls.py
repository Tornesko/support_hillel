from django.urls import path

from core.api import ApiTicket, ApiTicketsList

urlpatterns = [
    path("", ApiTicketsList.as_view(), name="tickets"),
    path("<int:id_>/", ApiTicket.as_view(), name="ticket"),
]
