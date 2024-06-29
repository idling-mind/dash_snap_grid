import React from 'react';

class DraggableDiv extends React.PureComponent {
    constructor(props) {
        super(props);
        this.onDragStart = this.onDragStart.bind(this);
    }

    onDragStart(event) {
        event.dataTransfer.setData('text/plain', this.props.id);
    }

    render() {
        return (
            <div
                id={this.props.id}
                draggable={true}
                unselectable="on"
                onDragStart={this.onDragStart}
                style={this.props.style}
            >
                {this.props.children}
            </div>
        );
    }
}

DraggableDiv.defaultProps = {};

DraggableDiv.propTypes = {
    /**
     * The ID of this component, used to identify dash components in callbacks
     */
    id: PropTypes.string,

    /**
     * The children of this component
     */
    children: PropTypes.node,

    /**
     * The style of this component
     */
    style: PropTypes.object,

    /**
     * Dash-assigned callback that gets fired when the input changes.
     * This callback will have the new value.
     * */
    setProps: PropTypes.func,
};

export default DraggableDiv;
