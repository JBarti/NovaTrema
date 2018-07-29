import React, { Component } from 'react'
import PropTypes from 'prop-types'
import './Image-lock.css'

class ImageBlock extends Component {
    render() {
        return (
            <div className='image-block' style={this.props.style} src=""></div>
        );
    }
}

ImageBlock.propTypes = {
    src: PropTypes
        .string
        .isRequired
}

export default ImageBlock