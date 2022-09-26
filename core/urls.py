from django.urls import path

from core.api import ApiTicket, ApiTicketsList, TicketAssignAPI


urlpatterns = [
    path("", ApiTicketsList.as_view(), name="tickets"),
    path("<int:pk>/", ApiTicket.as_view(), name="ticket"),
    path("<int:id>/assing/", TicketAssignAPI.as_view()),
]
