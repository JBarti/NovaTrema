import React, { Component } from 'react'
import PropTypes from 'prop-types'
import './Image-block.css'

class ImageBlock extends Component {

    render() {

        let imageBlockStyle = {
            width: this.props.width,
            height: this.props.height,
            backgroundImage: this.props.src
        }

        return (
            <div className='image-block' style={imageBlockStyle}>
                {this.props.children}
            </div>
        );
    }
}

ImageBlock.propTypes = {
    src: PropTypes
        .string
        .isRequired
}

export default ImageBlock