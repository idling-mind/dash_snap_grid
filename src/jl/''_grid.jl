# AUTO GENERATED FILE - DO NOT EDIT

export ''_grid

"""
    ''_grid(;kwargs...)
    ''_grid(children::Any;kwargs...)
    ''_grid(children_maker::Function;kwargs...)


A Grid component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The children of the grid
- `id` (String; optional): The ID used to identify this component in Dash callbacks
- `allowOverlap` (Bool; optional): allow overlapping in the grid
- `autoSize` (Bool; optional): If true, container size swells to fit contents
- `cols` (Real; optional): The number of columns in the grid
- `compactType` (a value equal to: 'vertical', 'horizontal', null; optional): Compaction type
- `containerPadding` (Array of Reals; optional): Padding inside the container [x, y] in px
- `draggableCancel` (String; optional): A CSS selector for tags that will not be draggable
Use this to so that some elements like buttons register clicks as expected
- `draggableHandle` (String; optional): A CSS selector for tags that will act as the draggable handle
- `droppedItem` (Dict; optional): ID of the dropped element
- `isBounded` (Bool; optional): Is bounded
- `isDraggable` (Bool; optional): Whether the grid items are draggable
- `isDroppable` (Bool; optional): if true, droppable elements (with draggable=true) can be dropped on the grid
droppedItem is the layout information of the dropped element
- `isResizable` (Bool; optional): Whether the grid items are resizable
- `layout` (Array of Dicts; optional): The layout of the grid
- `margin` (Array of Reals; optional): Margin between items [x, y] in px
- `persistLayout` (Bool; optional): The persistence of the layout. If set to true, the layout will be persisted in the local storage
and will be used when the component is loaded after pageload or refresh.
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
function ''_grid(; kwargs...)
        available_props = Symbol[:children, :id, :allowOverlap, :autoSize, :cols, :compactType, :containerPadding, :draggableCancel, :draggableHandle, :droppedItem, :isBounded, :isDraggable, :isDroppable, :isResizable, :layout, :margin, :persistLayout, :preventCollision, :resizeHandles, :rowHeight, :transformScale, :useCSSTransforms, :width]
        wild_props = Symbol[]
        return Component("''_grid", "Grid", "dash_snap_grid", available_props, wild_props; kwargs...)
end

''_grid(children::Any; kwargs...) = ''_grid(;kwargs..., children = children)
''_grid(children_maker::Function; kwargs...) = ''_grid(children_maker(); kwargs...)

