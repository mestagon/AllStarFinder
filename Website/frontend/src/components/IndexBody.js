import React, { Component } from "react";
import Model from "./Model";

class IndexBody extends Component {
    render() {
        return (
            <div className = "container" style = {{paddingTop: "70px", paddingBottom: "70px"}}>
              <h3>Introduction</h3>
              <p>
                This is a project I made to predict NBA All Stars of the 2018-2019 season using scikit-learn, a machine learning library. 
                NBA All Stars are NBA players who are selected to play in the annual All Star game. Players can be selected earning enough fan, player, and media votes or
                chosen by an NBA head coach. In total, there can be 24 all stars, 12 from the East and West conference respectively. These conferences are divided
                by the players teams' geographical location. In theory, this would mean All Star Players would make up the 12 best players of each conference.
                <br></br>
                Click <a href ="#model">here</a> to test it yourself!
              </p>
              <h3>Methodology</h3>
              <p>
                The first step I took was to collect enough data to use for my training model, which I got from basketball-reference.com. I chose to 
                include all player stats from the last 25 basketball seasons as a starting point for my training data. This is because the way the NBA is 
                played today is vastly different from previous eras. As such, including those data would likely hurt my predictions. Moreover, I wanted 
                enough data points so that my model could more accurately predict All Star players.
              </p>
              <h3>Feature Selection</h3>
              <p>
                Features are the qualities that we can use to predict if a player is an all star player.
                <br></br>
                <br></br>
                <div>G - The number of games played in the season. Voters and coaches believe that being good for only one game is not the same as being good for 50+ games.</div>
                <br></br>
                <div>GS - The number of games the player started in the season. If a player is good, coaches would want them to start the game more.</div>
                <br></br>
                <div>MP - Average number of minutes played in a game. Good players tend to play more.</div>
                <br></br>
                <div>FG - Average number of shots made in a game. Good players tend to shoot more.</div>
                <br></br>
                <div>FGA - Average number of shots taken in a game. Good players should also make more shots compared to an average or bad player.</div>
                <br></br>
                <div>eFG% - This is a formula used to calculate a field goal percentage (likelihood of scoring) by accounting for the fact that 2 point shots count more than 3 point shots The formula is given by (Field Goal Made + 0.5 * 3Point Shots Made)/Field Goal Attempts. Higher percentages are indicative of an all star player.</div>
                <br></br>
                <div>TRB - Average number of rebounds grabbed per game. Good players have a higher number of rebounds.</div>
                <br></br>
                <div>AST - Average number of assists in a game. Good players have a higher number of assists.</div>
                <br></br>
                <div>STL - Average number of steals in a game. Good players have high number of steals.</div>
                <br></br>
                <div>BLK - Average number of blocks in a game. Good players have high number of blocks.</div>
                <br></br>
                <div>PF - Average number of fouls conducted in a game. Fouls help opposing teams. Good players want to minimize fouls.</div>
                <br></br>
                <div>PTS - Average number of points scored in a game. Good players score more points.</div>
                <br></br>
                A high value in these stats are generally reflective of a good player with the exception of fouls beacause good players tend to foul less.
              </p>
              <h3>Results</h3>
              <p>
                After I collected relevant data, I trained my model using a KNeighborsClassifier. I then used my model on each of the players 
                from the 2018-2019 nba season to predict whether the player would be an all star. I then compared compared my prediction to whether
                the player was actually a player that season and found that I had a 97% accuracy rate with my model. 
              </p>
              <h3>Limitations</h3>
              <p>
                Though my model generally predicts all star caliber players, it has a hard time getting border-line all star players correct. This is
                likely due to voting bias or conference strength. For example, a player that plays for a popular team may be selected to be an all
                star over another qualified player since the player is more popular. Moreover, conference strength plays a role in all star selections.
                Since all stars are selected compared to their peers in the conference, a borderline player may not be an all star in a tougher conference.
                For example, maybe the 12th best player in the east conference was the 15th best player in the west conference. If the player played in the
                west, he might not be selected for the all star game.
              </p>
              <h3 id = "model">Model</h3>
              <p>Enter a hypothetical player stat and see whether our model would predict the player to be an all star!</p>
              <Model />
            </div>
        )
    }
}

export default IndexBody;