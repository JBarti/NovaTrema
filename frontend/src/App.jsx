import React, { Component } from 'react';
import './App.scss';
import AppBar from './common/appbar/AppBar.jsx'
import Button from './common/button/button.jsx'
import SearchBar from './common/search-bar/Search-bar.jsx'

class App extends Component {

  render() {

    const appBarSmallStyle = {
      paddingRight: "50px",
      paddingLeft: '50px'
    }

    return (
      <div className="App">
        <AppBar>
          <Button>Naslovnica</Button>
          <Button>Novosti</Button>
          <Button>O nama</Button>
          <Button>Informacije</Button>
          <Button>Natječaji</Button>
        </AppBar>
        <AppBar style={appBarSmallStyle}>
          <Button>Raspored sati</Button>
          <Button>Vremenik pismenih provjera</Button>
          <Button>Tlocrt škole</Button>
          <Button>Radno vrijeme školske knjiznice</Button>
          <Button>Primanja roditelja</Button>
        </AppBar>
      </div>
    );
  }
}

export default App;
