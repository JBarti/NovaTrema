import React, { Component } from 'react'
import PropTypes from 'prop-types'
import './Block.css'

class Block extends Component {

    render() {

        let style = {
            width: this.props.width,
            height: this.props.height,
            backgroundColor: this.props.backgroundColor,
        }

        return (
            <div className='block' style={this.props.style}>
                {this.props.children}
            </div >
        );
    }
}

Block.propTypes = {
    children: PropTypes
        .oneOfType([PropTypes.object, PropTypes.array])
        .isRequired,
}

export default Block