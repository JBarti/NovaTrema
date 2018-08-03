import React, { Component } from 'react';
import './App.css';
import AppBar from './common/appbar/AppBar.jsx'
import Button from './common/button/button.jsx'
import SearchBar from './common/search-bar/Search-bar.jsx'
import ImageBlock from './common/image-block/Image-block.jsx'
import Block from './common/block/Block.jsx'

class App extends Component {

  state = {

  }

  inputHandler = (event) => {
    this.setState({ [event.target.name]: event.target.value })
  }

  render() {

    const appBarBig = {
      backgroundColor: "#ffdd23",
      height: "60px"
    }

    const appBarSmallStyle = {
      paddingRight: "50px",
      paddingLeft: '50px',
      backgroundColor: "#3ab0b2",
      color: "white",
      height: "40px"
    }

    const buttonAppBarBigStyle = {
      ":hover": {
        borderBottomColor: "#3ab0b2"
      }
    }

    return (
      <div className="App">
        <ImageBlock></ImageBlock>
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
      </div >
    );
  }
}

export default App;
