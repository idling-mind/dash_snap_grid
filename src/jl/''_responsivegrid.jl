# AUTO GENERATED FILE - DO NOT EDIT

export ''_responsivegrid

"""
    ''_responsivegrid(;kwargs...)
    ''_responsivegrid(children::Any;kwargs...)
    ''_responsivegrid(children_maker::Function;kwargs...)


A ResponsiveGrid component.

Keyword arguments:
- `children` (optional): The children of the grid
- `id` (optional): The ID used to identify this component in Dash callbacks
- `allowOverlap` (optional): allow overlapping in the grid
- `autoSize` (optional): If true, container size swells to fit contents
- `breakpoints` (optional): breakpoints for responsive design
- `cols` (optional): The number of columns in the grid. This is an object with keys lg, md, sm, xs, xxs
- `compactType` (optional): Compaction type
- `containerPadding` (optional): Padding inside the container [x, y] in px. Can be an object with keys lg, md, sm, xs, xxs
and values [x, y]
- `draggableCancel` (optional): A CSS selector for tags that will not be draggable
Use this to so that some elements like buttons register clicks as expected
- `draggableHandle` (optional): A CSS selector for tags that will act as the draggable handle
- `isBounded` (optional): Is bounded
- `isDraggable` (optional): Whether the grid items are draggable
- `isResizable` (optional): Whether the grid items are resizable
- `layout` (optional): The layout of the grid, Readonly.
- `layouts` (optional): The layouts of the grid
- `margin` (optional): Margin between items [x, y] in px. Can be an object with keys lg, md, sm, xs, xxs
and values [x, y]
- `preventCollision` (optional): If true, grid items wont change position when being dragged over
- `resizeHandles` (optional): Which resize handles to display
s, e, w, n, se, ne, sw, nw
- `rowHeight` (optional): The row height of the grid. Default is 150.
- `setProps` (optional): Dash-assigned callback that should be called whenever any of the
properties change
- `transformScale` (optional): If parent DOM node of ResponsiveReactGridLayout or ReactGridLayout has "transform: scale(n)" css property,
we should set scale coefficient to avoid render artefacts while dragging.
- `useCSSTransforms` (optional): Uses CSS3 `translate()` instead of position top/left.
This makes about 6x faster paint performance
- `width` (optional): Initial width of the grid
"""
function ''_responsivegrid(; kwargs...)
        available_props = Symbol[:children, :id, :allowOverlap, :autoSize, :breakpoints, :cols, :compactType, :containerPadding, :draggableCancel, :draggableHandle, :isBounded, :isDraggable, :isResizable, :layout, :layouts, :margin, :preventCollision, :resizeHandles, :rowHeight, :transformScale, :useCSSTransforms, :width]
        wild_props = Symbol[]
        return Component("''_responsivegrid", "ResponsiveGrid", "dash_grid_layout", available_props, wild_props; kwargs...)
end

''_responsivegrid(children::Any; kwargs...) = ''_responsivegrid(;kwargs..., children = children)
''_responsivegrid(children_maker::Function; kwargs...) = ''_responsivegrid(children_maker(); kwargs...)

