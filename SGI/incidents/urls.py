# incidents/urls.py

from django.urls import path
from .api.views import IncidentListCreate  # Importer la vue de l'API
from .views import home, report_incident, list_incidents, admin_dashboard,report_success

urlpatterns = [
    path('', home, name='home'),  # Page d'accueil
    path('/', report_success, name='report_success'),  # Page d'accueil
    path('report/', report_incident, name='report_incident'),  # Page de signalement
    path('incidents/', list_incidents, name='list_incidents'),  # Page de consultation des incidents
     
    path('dashboard/', admin_dashboard, name='admin_dashboard'),  # Route pour le tableau de bord
    path('incidents/api/', IncidentListCreate.as_view(), name='incident-list-create'),  # Route pour l'API
    
]