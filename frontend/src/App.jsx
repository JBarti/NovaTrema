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
      height: "62.5px"
    }

    const appBarSmallStyle = {
      paddingRight: "50px",
      paddingLeft: '50px',
      backgroundColor: "#3ab0b2",
      color: "white",
      height: "46px"
    }

    const buttonAppBarBigStyle = {
      ":hover": {
        borderBottomColor: "#3ab0b2"
      }
    }

    const photoNewsDemoStyleTop = {
      marginBottom: "75px",
    }

    const photoNewsDemoStyle = {
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      flexDirection: "column"
    }

    const rowSecondDemoStyle = {
      marginTop: "120px",
    }

    const achievmentStyle = {
      flexDirection: "column"
    }

    const zooBlock = {
      position: "relative"
    }

    const competitionsBlock = {
      display: "flex",
      flexDirection: "row",
      justifyContent: "flex-end",
      alignItems: "center",
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
        <Block
          paddingTop="120px"
          paddingBottom="120px"
          paddingLeft="156px"
          paddingRight="156px"
          backgroundColor="lightBlue"
        >
          <ImageBlock height="429.75px" width="600.75px" />
          <div>
            <p className="intro-block__title">Dragi učenici, kolege, prijatelji!</p>
            <p className="intro-block__text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.</p>
          </div>
        </Block>
        <Block
          paddingTop="120px"
          paddingBottom="120px"
          paddingLeft="321px"
          paddingRight="321px"
          backgroundColor="lightCoral"
        >
          <div>
            <ImageBlock
              variant={Object.assign({}, photoNewsDemoStyle, photoNewsDemoStyleTop)}
              width="389.625px"
              height="279.375px">
              <p className="title">naslov</p>
              <p className="text text--newsDemo">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam metus magna, imperdiet sed ligula vitae, interdum pretium risus.</p>
            </ImageBlock>
            <ImageBlock
              variant={photoNewsDemoStyle}
              width="389.625px"
              height="279.375px">
              <p className="title">naslov</p>
              <p className="text text--newsDemo">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam metus magna, imperdiet sed ligula vitae, interdum pretium risus.</p>
            </ImageBlock>
          </div>
          <div style={rowSecondDemoStyle}>
            <ImageBlock
              variant={Object.assign({}, photoNewsDemoStyle, photoNewsDemoStyleTop)}
              width="389.625px"
              height="279.375px">
              <p className="title">naslov</p>
              <p className="text text--newsDemo">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam metus magna, imperdiet sed ligula vitae, interdum pretium risus.</p>
            </ImageBlock>
            <ImageBlock
              variant={photoNewsDemoStyle}
              width="389.625px"
              height="279.375px">
              <p className="title">naslov</p>
              <p className="text text--newsDemo">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam metus magna, imperdiet sed ligula vitae, interdum pretium risus.</p>
            </ImageBlock>
          </div>
        </Block>
        <Block
          paddingTop="80px"
          paddingBottom="40px"
          paddingLeft="150px"
          paddingRight="150px"
          backgroundColor="lightBlue"
          variant={achievmentStyle}
        >
          <div className="achievment-container">
            <div className="achievment">
              <ImageBlock height="115px" width="115px"></ImageBlock>
              <p className="title title--achievment">lorem ipsum</p>
              <p className="text">lorem ipsum</p>
            </div>
            <div className="achievment">
              <ImageBlock height="115px" width="115px"></ImageBlock>
              <p className="title title--achievment">lorem ipsum</p>
              <p className="text">lorem ipsum</p>
            </div>
            <div className="achievment">
              <ImageBlock height="115px" width="115px"></ImageBlock>
              <p className="title title--achievment">lorem ipsum</p>
              <p className="text">lorem ipsum</p>
            </div>
            <div className="achievment">
              <ImageBlock height="115px" width="115px"></ImageBlock>
              <p className="title title--achievment">lorem ipsum</p>
              <p className="text">lorem ipsum</p>
            </div>
          </div>
          <div className="navigation">
            <div className="navigation-ball navigation-ball--selected"></div>
            <div className="navigation-ball"></div>
            <div className="navigation-ball"></div>
          </div>
        </Block>
        <Block
          paddingTop="65px"
          paddingBottom="65px"
          paddingLeft="160px"
          paddingRight="160px"
          backgroundColor="lightCoral"
        >
          <ImageBlock width="258.75px" height="127.5px"></ImageBlock>
          <ImageBlock width="258.75px" height="127.5px"></ImageBlock>
          <ImageBlock width="258.75px" height="127.5px"></ImageBlock>
          <ImageBlock width="258.75px" height="127.5px"></ImageBlock>
        </Block>
        <Block variant={zooBlock}>
          <ImageBlock width="50vw" height="844.5px"></ImageBlock>
          <ImageBlock width="50vw" height="844.5px"></ImageBlock>
          <div className="text text--box text--box-zoo">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco</div>
        </Block>
        <Block>
          <ImageBlock width="100vw" height="844.5px" variant={competitionsBlock}>
            <div className="text text--box">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco</div>
          </ImageBlock>
        </Block>
      </div >
    );
  }
}

export default App;
