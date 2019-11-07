import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import unicodedata
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import os
import numpy as np

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

# loads basketball reference link of all star dates
def getAllStarDateDict( website, currentSeasonYear ):
    df = pd.read_html(website)[1]    
    
    #removes the all star games that haven't occured yet
    df = df.dropna(subset=["Result"])
    
    # gets only the season year and date the game occured
    df = df[["Year","Date"]]
    
    # gets index of all the years we aren't using so we can drop them
    index = df[ currentSeasonYear - df["Year"] > 25 ].index
    df = df.drop(index)
    
    
    # use this to iterate through entire dataframe
    firstIndex = df.first_valid_index()
    dfLength = len(df.index)
    
    # subtract one from all the year to get season year due to website and data differences
    for i in range(firstIndex, dfLength + firstIndex):
        df.loc[i, "Year"] = df.loc[i, "Year"] - 1
       
    # converts df into a dictionary
    allStarDateDict = pd.Series(df["Date"].values, index = df["Year"]).to_dict()
    
    return (allStarDateDict)

# get nba all star players for the season year
def getAllStars(allStarDateDict):
    
    allStarDict = {}
    
    # add an extra one to year due to difference in year
    for year in allStarDateDict:
        df = pd.read_html("https://www.basketball-reference.com/allstar/NBA_{}.html".format(year + 1))
        # df[1] holds west, df[2] holds east
        together = pd.concat([df[1], df[2]]).reset_index()
        # gets the players in the game
        together = together["Unnamed: 0_level_0"]
        # remove na non players
        together = together.dropna()
        
        # removes unnecessary rows
        index = together[ (together["Starters"] == "Reserves") | (together["Starters"] == "Team Totals")].index
        together = together.drop(index)
        
        # removes accent
        together["Starters"] = together["Starters"].apply(removeAccent)
        
    
        # changes all the stuff into a list 
        allStarPlayers = together["Starters"].values.tolist()
        
        # puts the year and maps it to players
        allStarDict.update({ year: allStarPlayers })
    
    # remove dirk and wade since they were honarym members
    allStarDict.get(2018).remove("Dirk Nowitzki")
    allStarDict.get(2018).remove("Dwyane Wade")
    
    return (allStarDict)

# checks if player is an all star
def isAllStar( player, allStars, year ):
    for allStar in allStars.get(year):
        if (allStar == player):
            return (True)
    return (False)


# loads players from website given years from allStarDateDict
def loadPlayers(allStars):
    
    playerDict = {}
    
    # gets the players from the season years of allStarDAteDict
    for year in allStars:
        # to get season "1991-1992" or 1991 you need to use 1992 
        df = pd.read_html("https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year + 1))
        
        df = df[0]
        
        # gets rid of "Player" as a value
        df = df[ df["Player"] != "Player"]
        
        # gets rid of duplicate names in player list 
        df = df.drop_duplicates(subset = "Player")
    
        # reformats the index
        df = df.reset_index().drop(columns=["index"])
        
        
        # takes only the necessary values
        df = df[["Player", "Pos", "G", "GS", "MP", "FG", "FGA", "eFG%", "TRB", "AST", "STL", "BLK", "PF", "PTS"]]
        
        # removes asterik
        df["Player"] = df["Player"].apply(removeAsterik)
        df["Player"] = df["Player"].apply(removeAccent)
        
#        print (type(allStars.get(year)))
        # checks if column is all star
        df["All Star"] = df["Player"].apply(isAllStar, args = (allStars, year))
        
        # gets rid of nan with 0
        df.fillna(0)
        
        df = df.reset_index()
        
        playerDict.update({ year: df })

    return (playerDict)

allStarDateDict = getAllStarDateDict("https://www.basketball-reference.com/allstar/", 2017)
allStars = getAllStars(allStarDateDict)
testing = loadPlayers(allStars) 
"""
for year in testing:
    testing.get(year).to_csv( os.path.join(os.path.dirname("__file__"), "Data", "Player Roster"," {}.csv".format(year)))

"""
"""
testing = {}

for year in allStarDateDict.keys():
    tmp = pd.read_csv( os.path.join(os.path.dirname("__file__"), "Data", "Player Roster"," {}.csv".format(year)))
#    print (tmp)
    tmp = tmp.drop(["Unnamed: 0"], axis = 1)
#    print (tmp)
    testing.update({ year: tmp})
"""

def createClassifier( playerRoster ):
    # creates our classifier
#    classifier = SVC()
    classifier = KNeighborsClassifier()
    
    featureTrain = pd.DataFrame()
    featureTest = pd.DataFrame()
    
    labelTrain = pd.DataFrame()
    labelTest = pd.DataFrame()
    
    # seperates data into testing and training
    for year in playerRoster:
        data = playerRoster.get(year)
        
        # get our features
        feature = data[["G", "GS", "MP", "FG", "FGA", "eFG%", "TRB", "AST", "STL", "BLK", "PF", "PTS"]]
        # get our labels
        label = data["All Star"]
        
        # puts 2018 into testing data and rest and training
        if year == 2018:
            featureTest = pd.concat([featureTest, feature])
            labelTest = pd.concat([labelTest, label])
            featureTest = featureTest.fillna(0)
            labelTest = labelTest.fillna(0)
        else:
            featureTrain = pd.concat([featureTrain, feature])
            labelTrain = pd.concat([labelTrain, label])
            featureTrain = featureTrain.fillna(0)
            labelTrain = labelTrain.fillna(0)
    
#    data = playerRoster.get(2018)
#    x = data[["G", "GS", "MP", "FG", "FGA", "FG%", "TRB", "AST", "STL", "BLK", "PF", "PTS"]]
#    x = x.fillna(0)
#    y = data["All Star"]
#    X_train, X_test, y_train, y_test = train_test_split(x, y)
    classifier = classifier.fit(featureTrain, labelTrain)
    prediction = classifier.predict(featureTest)
    
#    print (type(featureTest))
    # test which players predicted to be all stars
    featureTest.insert(len(featureTest.columns), "Prediction", prediction)
    featureTest.insert(len(featureTest.columns), "Actual", labelTest)
    featureTest.insert(0, "Player", playerRoster.get(2018)["Player"])
    newTest = featureTest[["Player", "Prediction", "Actual"]]
    
    # prints out predicted all star players
    print ("Predicted all star players")
    print(newTest[newTest["Prediction"] == True])
    
    # print out actual all star players
    print ("Actual all star players")
    print(newTest[newTest["Actual"] == True])
    
    print (accuracy_score(labelTest, prediction))
    return (classifier)

classifier = createClassifier( testing )
    
        
        
        
        
        
