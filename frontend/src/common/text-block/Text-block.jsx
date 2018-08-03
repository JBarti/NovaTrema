import React, { Component } from 'react'
import PropTypes from 'prop-types'
import './TextBlock.css'

class TextBlock extends Component {

    render() {

        let style = {
            width: this.props.width,
            height: this.props.height,
        }

        return (
            <div className='textBlock' style={style}>
                {this.props.children}
            </div >
        );
    }
}

TextBlock.propTypes = {
    children: PropTypes
        .string
        .isRequired,
}

export default TextBlock