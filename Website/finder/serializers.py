from rest_framework import serializers
from finder.models import *

class PlayerStatsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PlayerStats
        fields = "__all__"

class ActualAllStarsSerializer(serializers.ModelSerializer):
    Player = serializers.CharField(source = "Player.Player", read_only = True)

    Actual = serializers.BooleanField(source = "Player.Actual", read_only= True)

    Predicted = serializers.BooleanField(source = "Player.Prediction", read_only= True)
    class Meta: 
        model = ActualAllStars
        fields = "__all__"

class PredictedAllStarsSerializer(serializers.ModelSerializer):
    Player = serializers.CharField(source = "Player.Player", read_only = True)

    Actual = serializers.BooleanField(source = "Player.Actual", read_only= True)

    Predicted = serializers.BooleanField(source = "Player.Prediction", read_only= True)
    class Meta: 
        model = PredictedAllStars
        fields = "__all__"