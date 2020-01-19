import React, { Component } from "react";
import ReactDom from "react-dom";
import Header from "./components/Header";
import StatsTable from "./components/StatsTable";

class App extends Component {
    render() {
        return (
            <>
            <Header />
            <StatsTable PlayerStats = {PlayerStats} />
            </>
        )
    }
}

ReactDom.render(<App/>, document.getElementById('app'));