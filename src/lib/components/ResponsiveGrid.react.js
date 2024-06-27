import {all, o} from 'ramda';
import React from 'react';
import {Responsive, WidthProvider} from 'react-grid-layout';
import 'react-grid-layout/css/styles.css';

const ReactGridLayout = WidthProvider(Responsive);

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

    onLayoutChange(currentLayout, allLayouts) {
        this.props.setProps({layout: currentLayout, layouts: allLayouts});
    }

    render() {
        const {layout, setprops, ...otherProps} = this.props;
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
    cols: {lg: 12, md: 10, sm: 6, xs: 4, xxs: 2},
    compactType: null,
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
    breakpoints: {lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0},
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
     * The number of columns in the grid. This is an object with keys lg, md, sm, xs, xxs
     */
    cols: PropTypes.object,

    /**
     * Compaction type
     */
    compactType: PropTypes.oneOf(['vertical', 'horizontal', null]),

    /**
     * The layout of the grid, Readonly.
     */
    layout: PropTypes.arrayOf(PropTypes.object),

    /**
     * The layouts of the grid
     */
    layouts: PropTypes.object,

    /**
     * Margin between items [x, y] in px. Can be an object with keys lg, md, sm, xs, xxs
     * and values [x, y]
     */
    margin: PropTypes.arrayOf(PropTypes.number) || PropTypes.object,

    /**
     * Padding inside the container [x, y] in px. Can be an object with keys lg, md, sm, xs, xxs
     * and values [x, y]
     */
    containerPadding: PropTypes.arrayOf(PropTypes.number) || PropTypes.object,

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
     * breakpoints for responsive design
     */
    breakpoints: PropTypes.object,

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
