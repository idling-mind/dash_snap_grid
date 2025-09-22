# AUTO GENERATED FILE - DO NOT EDIT

export ''_responsivegrid

"""
    ''_responsivegrid(;kwargs...)
    ''_responsivegrid(children::Any;kwargs...)
    ''_responsivegrid(children_maker::Function;kwargs...)


A ResponsiveGrid component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The children of the grid
- `id` (String; optional): The ID used to identify this component in Dash callbacks
- `allowOverlap` (Bool; optional): allow overlapping in the grid
- `autoSize` (Bool; optional): If true, container size swells to fit contents
- `breakpoint` (String; optional): The current breakpoint
- `breakpoints` (Dict; optional): breakpoints for responsive design
- `col` (Real; optional): The current column count
- `cols` (Dict; optional): The number of columns in the grid. This is an object with keys lg, md, sm, xs, xxs
- `compactType` (a value equal to: 'vertical', 'horizontal', null; optional): Compaction type
- `containerPadding` (optional): Padding inside the container [x, y] in px. Can be an object with keys lg, md, sm, xs, xxs
and values [x, y]
- `draggableCancel` (String; optional): A CSS selector for tags that will not be draggable
Use this to so that some elements like buttons register clicks as expected
- `draggableHandle` (String; optional): A CSS selector for tags that will act as the draggable handle
- `droppedItem` (Dict; optional): ID of the dropped element
- `isBounded` (Bool; optional): Is bounded
- `isDraggable` (Bool; optional): Whether the grid items are draggable
- `isDroppable` (Bool; optional): if true, droppable elements (with draggable=true) can be dropped on the grid
droppedItem is the layout information of the dropped element
- `isResizable` (Bool; optional): Whether the grid items are resizable
- `layout` (Array of Dicts; optional): The layout of the grid, Readonly.
- `layouts` (Dict; optional): The layouts of the grid
- `margin` (optional): Margin between items [x, y] in px. Can be an object with keys lg, md, sm, xs, xxs
and values [x, y]
- `preventCollision` (Bool; optional): If true, grid items wont change position when being dragged over
- `resizeHandles` (Array of Strings; optional): Which resize handles to display
s, e, w, n, se, ne, sw, nw
- `rowHeight` (Real; optional): The row height of the grid. Default is 150.
- `transformScale` (Real; optional): If parent DOM node of ResponsiveReactGridLayout or ReactGridLayout has "transform: scale(n)" css property,
we should set scale coefficient to avoid render artefacts while dragging.
- `useCSSTransforms` (Bool; optional): Uses CSS3 `translate()` instead of position top/left.
This makes about 6x faster paint performance
- `width` (Real; optional): Initial width of the grid
"""
function ''_responsivegrid(; kwargs...)
        available_props = Symbol[:children, :id, :allowOverlap, :autoSize, :breakpoint, :breakpoints, :col, :cols, :compactType, :containerPadding, :draggableCancel, :draggableHandle, :droppedItem, :isBounded, :isDraggable, :isDroppable, :isResizable, :layout, :layouts, :margin, :preventCollision, :resizeHandles, :rowHeight, :transformScale, :useCSSTransforms, :width]
        wild_props = Symbol[]
        return Component("''_responsivegrid", "ResponsiveGrid", "dash_snap_grid", available_props, wild_props; kwargs...)
end

''_responsivegrid(children::Any; kwargs...) = ''_responsivegrid(;kwargs..., children = children)
''_responsivegrid(children_maker::Function; kwargs...) = ''_responsivegrid(children_maker(); kwargs...)

