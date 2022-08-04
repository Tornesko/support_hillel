from core.api import get_all_tickets
from django.urls import path

urlpatterns = [
    path("", get_all_tickets)
]