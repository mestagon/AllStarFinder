import React, { Component } from "react";

class Header extends Component {
    render() {
        return (
            <nav className = "navbar navbar-expand-sm navbar-light bg-light">
                <div className = "navbar-brand">AllStarFinder</div>
                
                <a className = "nav-link" href = "/">Home</a>

                <a className = "nav-link" href = "/results">Results</a>
                      
            </nav>
        )
    }
}

export default Header;