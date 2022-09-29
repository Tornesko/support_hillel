from django.urls import path

from core.api import (
    ApiTicket,
    ApiTicketsList,
    CommentsCreateAPI,
    CommentsListAPI,
    TicketAssignAPI,
)

urlpatterns = [
    # tickets urls
    path("", ApiTicketsList.as_view(), name="tickets"),
    path("<int:pk>/", ApiTicket.as_view(), name="ticket"),
    path("<int:id>/assing/", TicketAssignAPI.as_view()),
    # comments urls
    path("<int:ticket_id>/comments/", CommentsListAPI.as_view()),
    path("<int:ticket_id>/comments/create/", CommentsCreateAPI.as_view()),
]
