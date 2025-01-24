# incidents/forms.py

from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    """
    Formulaire pour signaler un incident.
    """
    class Meta:
        model = Incident
        fields = ['description', 'location', 'urgency']  # Champs à inclure dans le formulaire
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Décrivez l\'incident'}),
            'location': forms.TextInput(attrs={'placeholder': 'Adresse ou coordonnées'}),
            'urgency': forms.Select(),
        }