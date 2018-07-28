import React, { Component } from 'react'
import PropTypes from 'prop-types'
import Button from '../button/button.jsx'
import SearchBar from '../search-bar/search-bar'
import './AppBar.css'

class AppBar extends Component {

    state = {
        
    }

    inputHandler = (event) =>{
        this.setState({[event.target.name]: event.target.value})
    }

    render() {
        return (
            <div className='appbar'>
                <div className='appbar appbar__button-container'>
                    <Button>Cmarina</Button>
                    <Button>Cmarina</Button>
                    <Button>Cmarina</Button>
                    <Button>Cmarina</Button>
                    <Button>Cmarina</Button>
                    <Button>Cmarina</Button>
                    <Button>Cmarina</Button>
                </div>
                <SearchBar 
                    value={this.state.value} 
                    name='mirko' 
                    onChange={this.inputHandler}
                ></SearchBar>
                {this.props.children}
            </div >
        );
    }
}

AppBar.propTypes = {
    children: PropTypes
        .oneOfType([PropTypes.object, PropTypes.array])
        .isRequired,
}

export default AppBar