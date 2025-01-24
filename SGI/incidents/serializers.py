# incidents/serializers.py

from rest_framework import serializers
from .models import Incident

class IncidentSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Incident.
    Transforme les données du modèle en JSON et vice versa.
    """
    class Meta:
        model = Incident
        fields = ['id', 'description', 'location', 'urgency', 'status', 'created_at']  # Champs à inclure