import React, { Component } from "react";

class StatsTable extends Component {
    constructor(props) {
        super(props);
    }

    
    componentDidMount() {
        $(".sticky-header").floatThead({top:55});
    }
    
    render() {
        var rows = this.props.PlayerStats.map((PlayerStats, i) => {
            return (
                <tr key ={i}>
                    <td>{PlayerStats.Player}</td>
                    <td>{PlayerStats.G}</td>
                    <td>{PlayerStats.GS}</td>
                    <td>{PlayerStats.MP}</td>
                    <td>{PlayerStats.FG}</td>
                    <td>{PlayerStats.FGA}</td>
                    <td>{PlayerStats.eFG}</td>
                    <td>{PlayerStats.TRB}</td>
                    <td>{PlayerStats.AST}</td>
                    <td>{PlayerStats.STL}</td>
                    <td>{PlayerStats.BLK}</td>
                    <td>{PlayerStats.PF}</td>
                    <td>{PlayerStats.PTS}</td>
                    <td>{PlayerStats.Prediction}</td>
                    <td>{PlayerStats.Actual}</td>
                </tr>
            );            
        }) 
       
        return (
            <div className = "container" style = {{paddingTop: "70px"}}>
                <h3>2018-2019 Results</h3>
                <br></br>
                <table className = "table table-striped w-auto table-bordered sticky-header">
                    <thead>
                        <tr>
                            <th scope = "col" title = "Name">Player</th>
                            <th scope = "col" title = "Games">G</th>
                            <th scope = "col" title = "Games Started">GS</th>
                            <th scope = "col" title = "Minutes Played">MP</th>
                            <th scope = "col" title = "Field Goals Made">FG</th>
                            <th scope = "col" title = "Field Goal Attempts">FGA</th>
                            <th scope = "col" title = "Effective Field Goal %">eFG%</th>
                            <th scope = "col" title = "Rebounds">TRB</th>
                            <th scope = "col" title = "Assists">AST</th>
                            <th scope = "col" title = "Steals">STL</th>
                            <th scope = "col" title = "Blocks">BLK</th>
                            <th scope = "col" title = "Fouls">PF</th>
                            <th scope = "col" title = "Points">PTS</th>
                            <th scope = "col" title = "Prediction">Prediction</th>
                            <th scope = "col" title = "All Star">Actual</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rows}
                    </tbody>
                </table>
            </div>
        )
    }
}

export default StatsTable;