# AUTO GENERATED FILE - DO NOT EDIT

export ''_grid

"""
    ''_grid(;kwargs...)
    ''_grid(children::Any;kwargs...)
    ''_grid(children_maker::Function;kwargs...)


A Grid component.

Keyword arguments:
- `children` (optional): The children of the grid
- `id` (optional): The ID used to identify this component in Dash callbacks
- `allowOverlap` (optional): allow overlapping in the grid
- `autoSize` (optional): If true, container size swells to fit contents
- `cols` (optional): The number of columns in the grid
- `compactType` (optional): Compaction type
- `containerPadding` (optional): Padding inside the container [x, y] in px
- `isDraggable` (optional): Whether the grid items are draggable
- `isResizable` (optional): Whether the grid items are resizable
- `layout` (optional): The layout of the grid, Readonly.
- `margin` (optional): Margin between items [x, y] in px
- `preventCollision` (optional): If true, grid items wont change position when being dragged over
- `resizeHandles` (optional): Which resize handles to display
- `rowHeight` (optional): The row height of the grid
- `setProps` (optional): Dash-assigned callback that should be called whenever any of the
properties change
- `width` (optional): width of the grid
"""
function ''_grid(; kwargs...)
        available_props = Symbol[:children, :id, :allowOverlap, :autoSize, :cols, :compactType, :containerPadding, :isDraggable, :isResizable, :layout, :margin, :preventCollision, :resizeHandles, :rowHeight, :width]
        wild_props = Symbol[]
        return Component("''_grid", "Grid", "dash_grid_layout", available_props, wild_props; kwargs...)
end

''_grid(children::Any; kwargs...) = ''_grid(;kwargs..., children = children)
''_grid(children_maker::Function; kwargs...) = ''_grid(children_maker(); kwargs...)

