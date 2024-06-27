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
        const storedLayout = JSON.parse(
            window.localStorage.getItem('gridlayout')
        );
        console.log('stored', storedLayout);
        const layout = storedLayout ? storedLayout : this.generateLayout();
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

    onLayoutChange(layout) {
        window.localStorage.setItem('gridlayout', JSON.stringify(layout));
    }

    render() {
        return (
            <ReactGridLayout
                onLayoutChange={this.onLayoutChange}
                {...this.props}
            >
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
     * width of the grid
     */
    width: PropTypes.number,

    /**
     * If true, container size swells to fit contents
     * */
    autoSize: PropTypes.bool,

    /**
     * The number of columns in the grid
     */
    cols: PropTypes.number,

    /**
     * Compaction type
     */
    compactType: PropTypes.oneOf(['vertical', 'horizontal', null]),

    /**
     * Margin between items [x, y] in px
     */
    margin: PropTypes.arrayOf(PropTypes.number),

    /**
     * Padding inside the container [x, y] in px
     */
    containerPadding: PropTypes.arrayOf(PropTypes.number),

    /**
     * The row height of the grid
     */
    rowHeight: PropTypes.number,

    /**
     * The layout of the grid, Readonly.
     */
    layout: PropTypes.arrayOf(PropTypes.object),

    /**
     * allow overlapping in the grid
     */
    allowOverlap: PropTypes.bool,

    /**
     * If true, grid items wont change position when being dragged over
     */
    preventCollision: PropTypes.bool,

    /**
     * Which resize handles to display
     */
    resizeHandles: PropTypes.arrayOf(PropTypes.string),

    /**
     * Whether the grid items are draggable
     */
    isDraggable: PropTypes.bool,

    /**
     * Whether the grid items are resizable
     */
    isResizable: PropTypes.bool,

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
