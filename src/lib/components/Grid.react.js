import {o} from 'ramda';
import React from 'react';
import RGL, {WidthProvider} from 'react-grid-layout';
import 'react-grid-layout/css/styles.css';

const ReactGridLayout = WidthProvider(RGL);

class Grid extends React.PureComponent {
    constructor(props) {
        super(props);
        this.onLayoutChange = this.onLayoutChange.bind(this);
    }

    generateDOM() {
        const dom = this.props.children.map((child) => {
            return (
                <div key={child.props._dashprivate_layout.props.id}>
                    {child}
                </div>
            );
        });
        return dom;
    }

    onLayoutChange(layout) {
        this.props.setProps({layout: layout});
    }

    render() {
        const {setProps, ...otherProps} = this.props;
        return (
            <ReactGridLayout
                onLayoutChange={this.onLayoutChange}
                {...otherProps}
            >
                {this.generateDOM()}
            </ReactGridLayout>
        );
    }
}

Grid.defaultProps = {
    autoSize: true,
    cols: 12,
    compactType: null,
    layout: [],
    margin: [10, 10],
    containerPadding: [10, 10],
    rowHeight: 150,
    isDraggable: true,
    isResizable: true,
    isBounded: false,
    useCSSTransforms: true,
    transformScale: 1,
    allowOverlap: false,
    preventCollision: false,
    resizeHandles: ['se'],
};

Grid.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * Initial width of the grid
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
     * A CSS selector for tags that will not be draggable
     * Use this to so that some elements like buttons register clicks as expected
     * */
    draggableCancel: PropTypes.string,

    /**
     * A CSS selector for tags that will act as the draggable handle
     * */
    draggableHandle: PropTypes.string,

    /**
     * Compaction type
     */
    compactType: PropTypes.oneOf(['vertical', 'horizontal', null]),

    /**
     * The layout of the grid
     */
    layout: PropTypes.arrayOf(PropTypes.object),

    /**
     * Margin between items [x, y] in px
     */
    margin: PropTypes.arrayOf(PropTypes.number),

    /**
     * Padding inside the container [x, y] in px
     */
    containerPadding: PropTypes.arrayOf(PropTypes.number),

    /**
     * The row height of the grid. Default is 150.
     */
    rowHeight: PropTypes.number,

    /**
     * Whether the grid items are draggable
     */
    isDraggable: PropTypes.bool,

    /**
     * Whether the grid items are resizable
     */
    isResizable: PropTypes.bool,

    /**
     * Is bounded
     * */
    isBounded: PropTypes.bool,

    /**
     * Uses CSS3 `translate()` instead of position top/left.
     * This makes about 6x faster paint performance
     * */
    useCSSTransforms: PropTypes.bool,

    /**
     * If parent DOM node of ResponsiveReactGridLayout or ReactGridLayout has "transform: scale(n)" css property,
     * we should set scale coefficient to avoid render artefacts while dragging.
     * */
    transformScale: PropTypes.number,

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
     * s, e, w, n, se, ne, sw, nw
     */
    resizeHandles: PropTypes.arrayOf(PropTypes.string),

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
