import React, { Component } from 'react'
import PropTypes from 'prop-types'
import './SearchBar.css'

class SearchBar extends Component {
    render() {
        const { placeholder, name, onChange, value } = this.props
        return (
            <input className="search-bar"
                name={name}
                value={value}
                onChange={onChange}
                placeholder={placeholder ? placeholder : 'Search'}
            />
        );
    }
}

export default SearchBar