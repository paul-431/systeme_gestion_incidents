# incidents/api/views.py

from rest_framework import generics
from rest_framework.response import Response
from .serializers import IncidentSerializer
from incidents.models import Incident

class IncidentListCreate(generics.ListCreateAPIView):
    """
    Vue API pour lister et créer des incidents.
    """
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            incident = serializer.save()
            # Notifier le tableau de bord ou toute autre logique
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)