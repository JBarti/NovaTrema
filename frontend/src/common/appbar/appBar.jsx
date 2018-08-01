import React, { Component } from 'react'
import PropTypes from 'prop-types'
import Button from '../button/button.jsx'
import SearchBar from '../search-bar/Search-bar.jsx'
import './AppBar.css'
import '../search-bar/SearchBar.css'

class AppBar extends Component {

    render() {
        return (
            <div className='appbar' style={this.props.style}>
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