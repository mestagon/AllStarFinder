import pandas as pd
from finder.models import *
#import os

# f = os.path.join(os.path.dirname("__file__"), "Results", "results2018.csv")

# get the results
# results2018 = pd.read_csv(f, index_col = 0, encoding = "utf-8")
results2018 = pd.read_csv("finder/Results/results2018.csv", index_col = 0)
predicted2018 = pd.read_csv("finder/Results/predicted2018.csv", index_col = 0)
actual2018 = pd.read_csv("finder/Results/actual2018.csv", index_col = 0)

# convert it to a dict
results2018 = results2018.to_dict("index")
predicted2018 = predicted2018.to_dict("index")
actual2018 = actual2018.to_dict("index")

# create the models
modelInstances = [ PlayerStats( ID = playerId, Player = results2018.get(playerId).get("Player"),
                                G = results2018.get(playerId).get("G"), GS = results2018.get(playerId).get("GS"), 
                                MP = results2018.get(playerId).get("MP"), FG = results2018.get(playerId).get("FG"),
                                FGA = results2018.get(playerId).get("FGA"), eFG = results2018.get(playerId).get("eFG%"),
                                TRB = results2018.get(playerId).get("TRB"), AST = results2018.get(playerId).get("AST"),
                                STL = results2018.get(playerId).get("STL"), BLK = results2018.get(playerId).get("BLK"),
                                PF = results2018.get(playerId).get("PF"), PTS = results2018.get(playerId).get("PTS"),
                                Prediction = results2018.get(playerId).get("Prediction"),
                                Actual = results2018.get(playerId).get("Actual"),
                                ) for playerId in results2018
                        
        ]

#PlayerStats.objects.bulk_create(modelInstances)

for playerId in actual2018:
    tmp = ActualAllStars(Player = PlayerStats.objects.get(pk = playerId))
    tmp.save()

for playerId in predicted2018:
    tmp = PredictedAllStars(Player = PlayerStats.objects.get(pk = playerId))
    tmp.save()