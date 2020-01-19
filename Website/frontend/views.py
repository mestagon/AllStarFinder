from django.shortcuts import render
from finder.models import PlayerStats
from finder.serializers import PlayerStatsSerializer, PredictedAllStars, ActualAllStars
from django.http import JsonResponse, HttpResponse
import json
import pickle
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import os
import numpy as np

currDir = os.path.dirname(__file__)
# open classifier
classifier = pickle.load(open(os.path.join(currDir, "classifier.sav"), 'rb'))

# Create your views here.
def index(request):
    return (render(request, "frontend/index.html"))

def results(request):
    stats = []
    for player in PlayerStats.objects.all():
        d = {"ID": player.ID, "Player": player.Player, "G": player.G, "GS": player.GS, "MP": float(player.MP),
                              "FG": float(player.FG), "FGA": float(player.FGA), "eFG": float(player.eFG), "TRB": float(player.TRB), "AST": float(player.AST),
                              "STL": float(player.STL), "BLK": float(player.BLK), "PF": float(player.PF), "PTS": float(player.PTS), 
                              "Prediction": "YES" if player.Prediction else "NO",
                              "Actual": "YES" if player.Actual else "NO"}

        stats.append(d)
    context = {
        "PlayerStats": json.dumps(stats)
    }

    return (render(request, "frontend/results.html", context = context))

def predict(request):
    print ("hi")
    
    # get data
    G = float(request.POST.get("G"))
    GS = float(request.POST.get("GS"))
    MP = float(request.POST.get("MP"))
    FG = float(request.POST.get("FG"))
    FGA = float(request.POST.get("FGA"))
    eFG = float(request.POST.get("eFG"))
    TRB = float(request.POST.get("TRB"))
    AST = float(request.POST.get("AST"))
    STL = float(request.POST.get("STL"))
    BLK = float(request.POST.get("BLK"))
    PF = float(request.POST.get("PF"))
    PTS = float(request.POST.get("PTS"))

    dataframe = pd.DataFrame( data = {"G": G, "GS": GS, "MP": MP, "FG": FG, "FGA": FGA,
                                      "eFG%": eFG, "TRB": TRB, "AST": AST, "STL": STL,
                                      "BLK": BLK, "PF": PF, "PTS": PTS},
                              columns = ["G", "GS", "MP", "FG", "FGA", "eFG%", "TRB", "AST", "STL", "BLK", "PF", "PTS"],
                              index = [0]
                            )


    
    result = classifier.predict(dataframe)
    result = result.astype(str)

    prediction = result[0]
    prediction = "True" if prediction == "True" else "False"

    return (JsonResponse({"prediction": prediction}))
   