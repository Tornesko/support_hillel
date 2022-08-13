from django.urls import path

from core.api import ApiTicketsList, ApiTicket

urlpatterns = [
    path("", ApiTicketsList.as_view(), name="tickets"),
    path("<int:id_>/", ApiTicket.as_view(), name="ticket"),
]
