# incidents/urls.py

from django.urls import path
from .views import IncidentListCreate

urlpatterns = [
    path('incidents/api/', IncidentListCreate.as_view(), name='incident-list-create'),  # Route pour l'API
]