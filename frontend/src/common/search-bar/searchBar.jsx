import React, { Component } from 'react'
import PropTypes from 'prop-types'

class SearchBar extends Component {
    render() {
        return (
            <input
                name={this.props.name}
                value={this.props.value}
                onChange={this.props.onChange}
                placeholder={this.props.placeholder ? this.props.placeholder : 'Search'}
                style={this.props.style}
            />
        );
    }
}

export default SearchBar