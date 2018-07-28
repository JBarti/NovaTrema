import React, { Component } from 'react'
import PropTypes from 'prop-types'
import './button.css'

class Button extends Component {
    render() {
        return (
            <div className='button' style={this.props.style}>
                {this.props.children}
            </div>
        );
    }
}

Button.propTypes = {
    children: PropTypes
        .string
        .isRequired
}

export default Button