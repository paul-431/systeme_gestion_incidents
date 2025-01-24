# incidents/models.py

from django.db import models

class Incident(models.Model):
    """
    Modèle représentant un incident signalé par un client.
    """
    URGENCY_CHOICES = [
        ('low', 'Faible'),
        ('medium', 'Moyen'),
        ('high', 'Élevé'),
    ]

    description = models.TextField()  # Description de l'incident
    location = models.CharField(max_length=255)  # Localisation de l'incident
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES)  # Niveau d'urgence
    status = models.CharField(max_length=10, default='open')  # Statut de l'incident
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création

    def __str__(self):
        return f"{self.description} - {self.status}"
