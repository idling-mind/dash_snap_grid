import React, {Component} from 'react';
import GridLayout from 'react-grid-layout';
import 'react-grid-layout/css/styles.css';
import PropTypes from 'prop-types';

class GridItem extends Component {
    render() {
        const {id, children, setProps} = this.props;
        return (
            <div id={id} style={this.props.style}>
                {children}
            </div>
        );
    }
}

GridItem.defaultProps = {
    style: {},
};

GridItem.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * The children of the grid
     */
    children: PropTypes.node,

    /**
     * The x position of the grid item
     */
    x: PropTypes.number,

    /**
     * The y position of the grid item
     */
    y: PropTypes.number,

    /**
     * The width of the grid item
     */
    width: PropTypes.number,

    /**
     * The height of the grid item
     */
    height: PropTypes.number,

    /**
     * Whether the grid item is static (non-draggable and non-resizable)
     */
    static: PropTypes.bool,

    /**
     * The minimum width of the grid item
     */
    min_width: PropTypes.number,

    /**
     * The minimum height of the grid item
     */
    min_height: PropTypes.number,

    /**
     * The maximum width of the grid item
     */
    max_width: PropTypes.number,

    /**
     * The maximum height of the grid item
     */
    max_height: PropTypes.number,

    /**
     * Whether the grid item is draggable
     */
    draggable: PropTypes.bool,

    /**
     * Whether the grid item is resizable
     */
    resizable: PropTypes.bool,

    /**
     * Whether the grid item is bounded within the grid container
     */
    bounded: PropTypes.bool,

    /**
     * The style of the grid item
     */
    style: PropTypes.object,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func,
};

export default GridItem;
