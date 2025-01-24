# incidents/views.py

import requests
from django.shortcuts import render
from .forms import IncidentForm  # Import du formulaire
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Incident
from .serializers import IncidentSerializer

def home(request):
    """
    Vue pour la page d'accueil.
    """
    return render(request, 'incidents/home.html')

def report_success(request):
    """
    Vue pour la page d'accueil.
    """
    return render(request, 'incidents/home.html')


def report_incident(request):
    """
    Vue pour le signalement d'un incident.
    Cette vue envoie les données à l'API REST.
    """
    if request.method == 'POST':
        form = IncidentForm(request.POST)  # Crée un formulaire avec les données POST
        if form.is_valid():  # Vérifie la validité du formulaire
            # Prépare les données pour l'API
            incident_data = {
                'description': form.cleaned_data['description'],
                'location': form.cleaned_data['location'],
                'urgency': form.cleaned_data['urgency'],
            }
            # Envoie les données à l'API REST
            response = requests.post('http://127.0.0.1:8000/incidents/api/', json=incident_data)
            
            #print(response.__content__)

            if response.status_code == 201:  # Si l'incident a été créé avec succès
                return render(request, 'incidents/report_success.html')  # Affiche la confirmation
            else:
                form.add_error(None, 'Erreur lors du signalement de l\'incident.')  # Gère l'erreur de l'API
    else:
        form = IncidentForm()  # Affiche un formulaire vide

    return render(request, 'incidents/report_incident.html', {'form': form})

def list_incidents(request):
    """
    Vue pour la consultation des incidents.
    """
    incidents = Incident.objects.all()  # Récupère tous les incidents
    return render(request, 'incidents/list_incidents.html', {'incidents': incidents})

def admin_dashboard(request):
    """
    Vue pour le tableau de bord de l'administrateur.
    Affiche tous les incidents signalés.
    """
    incidents = Incident.objects.all()  # Récupère tous les incidents
    return render(request, 'incidents/admin_dashboard.html', {'incidents': incidents})


    def notify_admin_dashboard(self, incident):
        """
        Fonction pour notifier le tableau de bord de l'administrateur.
        Vous pouvez mettre en œuvre une logique ici, comme envoyer un email
        ou mettre à jour une interface.
        """
        # Exemple de notification (logique à personnaliser selon vos besoins)
        print(f"Un nouvel incident a été signalé: {incident.description}")

