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
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.cache import cache
import unicodedata
import time

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

@ensure_csrf_cookie
def findPlayer(request):
 
    # find what is entered in search query
    search = request.POST.get("Player")
    
    search = search.lower()

    # split by comma, first word should be player name and second is year
    result = search.split(",")

    name = result[0]
    name = removeAsterik(name)
    name = removeAccent(name)

    # only want last 4 characters
    year = result[1][-4:]

    k = name + " " + year

    k = k.replace(" ", "_")

    match = cache.get(k)

    # start_time = time.time()
    
    start_time = int(round(time.time() * 1000))
          
      # if we don't have cache then get information
    if not match:
        df = pd.read_html("https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year))

        df = df[0]
        
        
        # fix text to be consistent
        df["Player"] = df["Player"].apply(removeAsterik)
        df["Player"] = df["Player"].apply(removeAccent)
        df["Player"] = df["Player"].str.lower()

        df = df[ df["Player"] == name]
        
        if (len(df) == 0):
            return JsonResponse({"error": "No Player Found"})

        # get rid of dup
        df = df.drop_duplicates(subset = "Player")

        df = df[["G", "GS", "MP", "FG", "FGA", "eFG%", "TRB", "AST", "STL", "BLK", "PF", "PTS"]]

        d = df.to_dict(orient = 'records')
        
        
        cache.set(k, d[0], 2400)

        match = d[0]
      
    print ("My program took", int(round(time.time() * 1000)) - start_time, "to run")
    return JsonResponse({"match": match})

# removes asterik
def removeAsterik( string ):
    return (string.replace("*", ""))

# removes accent from characters
def removeAccent( text ):
    try:
        text = unicode(text, "utf-8")
    except NameError:
        pass
    
    text = unicodedata.normalize("NFD", text).encode("ascii", "ignore").decode("utf-8")
    
    return (text)

def generateKey(text):
    text = text.lower()
    text = text + " " + "2009"
    return text.replace(" ", "_"
