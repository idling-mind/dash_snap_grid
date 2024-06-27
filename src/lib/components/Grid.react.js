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

Grid.defaultProps = {
    isDraggable: true,
    isResizable: true,
    autoSize: true,
    allowOverlap: false,
    preventCollision: false,
    resizeHandles: ['se'],
    margin: [10, 10],
    containerPadding: [10, 10],
    rowHeight: 150,
    cols: 12,
    layout: [],
};

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
