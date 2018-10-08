import React, { Component } from 'react'
import './novosti.css'
import AppBar from '../../common/appbar/appBar'
import Button from '../../common/button/button'
import SearchBar from '../../common/search-bar/searchBar'


class Novosti extends Component {

    state = {}

    inputHandler = (event) => {
        this.setState({ [event.target.name]: event.target.value })
    }

    render() {

        const appBarBig = {
            backgroundColor: "gray",
            height: "62.5px"
        }

        const appBarSmallStyle = {
            paddingRight: "50px",
            paddingLeft: '50px',
            backgroundColor: "lightgray",
            color: "white",
            height: "46px",
        }

        const buttonAppBarBigStyle = {
            ":hover": {
                borderBottomColor: "#3ab0b2"
            }
        }

        return (
            <div>
                <AppBar style={appBarBig}>
                    <Button style={buttonAppBarBigStyle}>Naslovnica</Button>
                    <Button style={buttonAppBarBigStyle}>Novosti</Button>
                    <Button style={buttonAppBarBigStyle}>O nama</Button>
                    <Button style={buttonAppBarBigStyle}>Informacije</Button>
                    <Button style={buttonAppBarBigStyle}>Natječaji</Button>
                    <SearchBar
                        value={this.state.value}
                        name='appBar1'
                        onChange={this.inputHandler}
                    ></SearchBar>
                </AppBar>
                <AppBar style={appBarSmallStyle}>
                    <Button>Raspored sati</Button>
                    <Button>Vremenik pismenih provjera</Button>
                    <Button>Tlocrt škole</Button>
                    <Button>Radno vrijeme školske knjiznice</Button>
                    <Button>Primanja roditelja</Button>
                </AppBar>
                <div className="content">
                    <div className="tag-bar">
                        <SearchBar
                            value={this.state.value}
                            name='tagBar1'
                            onChange = {this.inputHandler}
                            placeholder = "#"
                        >
                        </SearchBar>
                        <div className="tag-bar__result"></div>
                    </div>
                </div>

            </div>
        );
    }
}
export default Novosti