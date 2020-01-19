from finder.models import PlayerStats
from rest_framework import viewsets, permissions
from .serializers import *

class PlayerStatsViewSets(viewsets.ModelViewSet):
    queryset = PlayerStats.objects.all()
    permissions = [permissions.AllowAny]
    serializer_class = PlayerStatsSerializer

class ActualAllStarsViewSets(viewsets.ModelViewSet):
    queryset = ActualAllStars.objects.all()
    permissions = [permissions.AllowAny]
    serializer_class = ActualAllStarsSerializer

class PredictedAllStarsViewSets(viewsets.ModelViewSet):
    queryset = PredictedAllStars.objects.all()
    permissions = [permissions.AllowAny]
    serializer_class = PredictedAllStarsSerializer