import React, { Component } from "react";
import PredictionResults from "./PredictionResults";

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var CSRF_TOKEN = getCookie('csrftoken');

class Model extends Component {
    constructor(props) {
        super(props);
        this.state = {
            G: "",
            GS: "",
            MP: "",
            FG: "",
            FGA: "",
            eFG: "",
            TRB: "",
            AST: "",
            STL: "",
            BLK: "",
            PF: "",
            PTS: "",
            RenderText: "",
            buttonDisabled: true,
            Player: ""
        }
    }


    handleChange = event => {
        // check if value entered is a number
        if (isNaN(event.target.value) || event.target.value === " ") {
            return;
        } else {
            this.setState({
                [event.target.name] : event.target.value
            })
        }
    }
    
    // check if button should be disabled
    isDisabled = () => {
        const {G, GS, MP, FG, FGA,  eFG, TRB, AST, STL, BLK, PF, PTS} = this.state;

        return !(G && GS && MP && FG && FGA && eFG && TRB && AST && STL && BLK && PF && PTS)
    }

    buttonClickHandler = () => {
        this.setState({
            RenderText: "Predicting..."
        })
        // get the current state values
        const {G, GS, MP, FG, FGA,  eFG, TRB, AST, STL, BLK, PF, PTS} = this.state;

        // make new xmlhttp request
        const request = new XMLHttpRequest();

        request.open("POST", "/predict");
        
        request.onload = () => {
            // get prediction
            const result = JSON.parse(request.responseText); 
            const text = result.prediction === "True" ? "This player is predicted to be an all star player" : "This player is not predicted to be an all star player"
            this.setState({
                RenderText: text
            })
        }
        
        // send data to servers
        const data = new FormData();
        data.append("G", G);
        data.append("GS", GS);
        data.append("MP", MP);
        data.append("FG", FG);
        data.append("FGA", FGA);
        data.append("eFG", eFG);
        data.append("TRB", TRB);
        data.append("AST", AST);
        data.append("STL", STL);
        data.append("BLK", BLK);
        data.append("PF", PF);
        data.append("PTS", PTS);
        request.setRequestHeader('X-CSRFToken', CSRF_TOKEN);
        request.send(data);
    }

    handleClick = () => {
      const {Player} = this.state;

      // make new xmlhttp request
      const request = new XMLHttpRequest();

      request.open("POST", "/find");
      
      request.onload = () => {
          // get prediction
          const result = JSON.parse(request.responseText); 
          console.log(result);
          console.log(result["match"]);
          
          console.log(result["match"]["G"]);
          if (result["match"]) {
              this.setState({
                  G: result["match"]["G"],
                  GS: result["match"]["GS"],
                  MP: result["match"]["MP"],
                  FG: result["match"]["FG"],
                  FGA: result["match"]["FGA"],
                  eFG: result["match"]["eFG%"],
                  TRB: result["match"]["TRB"],
                  AST: result["match"]["AST"],
                  STL: result["match"]["STL"],
                  BLK: result["match"]["BLK"],
                  PF: result["match"]["PF"],
                  PTS: result["match"]["PTS"],
                  SearchText: "Search Successful"
              });
          } 

          
          /*
          const text = result.prediction === "True" ? "This player is predicted to be an all star player" : "This player is not predicted to be an all star player"
          this.setState({
              RenderText: text
          })
          */
      }
      
      // send data to servers
      const data = new FormData();
      data.append("Player", Player);
      
      request.setRequestHeader('X-CSRFToken', CSRF_TOKEN);
      request.send(data);
    }

    updatePlayer = event => {
        this.setState({
            [event.target.name] : event.target.value
        })
    }

    render() {
        return (
            <div>
              
                <div class="input-group" style = {{width: "400px", marginBottom: "10px"}}>
                    <input class="form-control" 
                           placeholder = "E.g. Kobe Bryant, 2008-2009" 
                           name = "Player" 
                           value = {this.state.Player} 
                           onChange = {this.updatePlayer}/>
                    <span class="input-group-btn">
                        <button class="btn btn-info" style = {{marginLeft: "0px"}} onClick ={this.handleClick}>Search</button>
                    </span>
                </div>
                
                <label htmlFor = "G">
                    Games Played in Season:
                    <input 
                        name = "G" 
                        value = {this.state.G} 
                        onChange = {this.handleChange}
                    />
                </label>
                

                <label htmlFor = "GS">
                    Games Started in Season:
                    <input 
                        name = "GS" 
                        value = {this.state.GS}
                        onChange = {this.handleChange}
                    />
                </label>
                
                <label htmlFor = "MP">
                    Average Minutes per Game:
                    <input 
                        name = "MP" 
                        value = {this.state.MP}
                        onChange = {this.handleChange}
                    />
                </label>
                
                <label htmlFor = "FG">
                    Average Field Goals Made:
                    <input 
                        name = "FG" 
                        value = {this.state.FG}
                        onChange = {this.handleChange}
                    />
                </label>

                <label htmlFor = "FGA">
                    Average Field Goal Attempts:
                    <input 
                        name = "FGA" 
                        value = {this.state.FGA}
                        onChange = {this.handleChange}
                    />
                </label>

                <label htmlFor = "eFG">
                    Effective Field Goal Percentage:
                    <input 
                        name = "eFG" 
                        value = {this.state.eFG}
                        onChange = {this.handleChange}
                    />
                </label>

                <label htmlFor = "TRB">
                    Average Rebounds per Game:
                    <input 
                        name = "TRB" 
                        value = {this.state.TRB}
                        onChange = {this.handleChange}
                    />
                </label>

                <label htmlFor = "AST">
                    Average Assists per Game:
                    <input 
                        name = "AST" 
                        value = {this.state.AST}
                        onChange = {this.handleChange}
                    />
                </label>

                <label htmlFor = "STL">
                    Average Steals per Game:
                    <input 
                        name = "STL" 
                        value = {this.state.STL}
                        onChange = {this.handleChange}
                    />
                </label>

                <label htmlFor = "BLK">
                    Average Blocks per Game:
                    <input 
                        name = "BLK" 
                        value = {this.state.BLK}
                        onChange = {this.handleChange}
                    />
                </label>

                <label htmlFor = "PF">
                    Average Fouls per Game:
                    <input 
                        name = "PF" 
                        value = {this.state.PF}
                        onChange = {this.handleChange}
                    />
                </label>

                <label htmlFor = "PTS">
                    Average Points per Game:
                    <input 
                        name = "PTS" 
                        value = {this.state.PTS}
                        onChange = {this.handleChange}
                    />
                </label>
                <button 
                    className ="btn btn-primary" 
                    disabled = {this.isDisabled()}
                    onClick = {this.buttonClickHandler}
                > 
                    Predict
                </button>
                {this.state.RenderText ? <PredictionResults text = {this.state.RenderText}/> : null}
            </div>  
        )
    }
}


export default Model;
