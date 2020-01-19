import React, { Component } from "react";
import ReactDom from "react-dom";
import Header from "./components/Header";
import IndexBody from "./components/IndexBody";


class App extends Component {
    render() {
        return (
            <>
            <Header />
            <IndexBody />
            </>
        )
    }
}

ReactDom.render(<App/>, document.getElementById('app'));