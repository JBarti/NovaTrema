import React, { Component } from 'react'
import PropTypes from 'prop-types'
import './Block.css'

class Block extends Component {

    render() {

        let style = {
            paddingTop: this.props.paddingTop,
            paddingBottom: this.props.paddingBottom,
            paddingLeft: this.props.paddingLeft,
            paddingRight: this.props.paddingRight,
            backgroundColor: this.props.backgroundColor,
        }

        return (
            <div className='block' style={style}>
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