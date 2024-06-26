import React from 'react';
import _ from 'lodash';
import RGL, {WidthProvider} from 'react-grid-layout';

const ReactGridLayout = WidthProvider(RGL);

class Grid extends React.PureComponent {
    static defaultProps = {
        isDraggable: true,
        isResizable: true,
        rowHeight: 30,
        cols: 12,
    };

    generateDOM() {
        // Generate items with properties from the layout, rather than pass the layout directly
        const layout = this.generateLayout();
        return layout.map((l, i) => {
            return (
                <div key={l.i} data-grid={l}>
                    {this.props.children[i]}
                </div>
            );
        });
    }

    generateLayout() {
        const defaults = {
            x: 0,
            y: 0,
            width: 1,
            height: 1,
            min_width: 1,
            min_height: 1,
            max_width: Infinity,
            max_height: Infinity,
            draggable: true,
            resizable: true,
            bounded: false,
        };

        return this.props.children.map(function (child) {
            console.log(child);
            const childProps = child.props._dashprivate_layout.props;
            const result = Object.keys(defaults).reduce(
                (acc, key) => {
                    // Convert the key to the expected format, if necessary
                    const propKey =
                        key === 'width'
                            ? 'w'
                            : key === 'height'
                            ? 'h'
                            : key === 'min_width'
                            ? 'minW'
                            : key === 'min_height'
                            ? 'minH'
                            : key === 'max_width'
                            ? 'maxW'
                            : key === 'max_height'
                            ? 'maxH'
                            : key === 'draggable'
                            ? 'isDraggable'
                            : key === 'resizable'
                            ? 'isResizable'
                            : key === 'bounded'
                            ? 'isBounded'
                            : key;

                    // Check if the property is defined; if not, use the default value
                    acc[propKey] =
                        childProps[key] !== undefined
                            ? childProps[key]
                            : defaults[key];

                    return acc;
                },
                {i: childProps.id}
            ); // Initialize accumulator with the 'i' property set to childProps.id
            return result;
        });
    }

    // onLayoutChange(layout) {
    //     this.props.onLayoutChange(layout);
    // }

    render() {
        return (
            <ReactGridLayout {...this.props}>
                {this.generateDOM()}
            </ReactGridLayout>
        );
    }
}

Grid.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * The number of columns in the grid
     */
    cols: PropTypes.number,

    /**
     * The row height of the grid
     */
    rowHeight: PropTypes.number,

    /**
     * The layout of the grid
     * This is an array of objects, see the demo for more complete usage
     */
    layout: PropTypes.arrayOf(PropTypes.object),

    /**
     * Whether the grid items are draggable
     */
    isDraggable: PropTypes.bool,

    /**
     * Whether the grid items are resizable
     */
    isResizable: PropTypes.bool,

    /**
     * The callback that is fired when the layout changes
     */
    onLayoutChange: PropTypes.func,

    /**
     * The children of the grid
     */
    children: PropTypes.node,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func,
};

export default Grid;
