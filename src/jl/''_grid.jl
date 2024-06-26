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
- `cols` (optional): The number of columns in the grid
- `isDraggable` (optional): Whether the grid items are draggable
- `isResizable` (optional): Whether the grid items are resizable
- `layout` (optional): The layout of the grid
This is an array of objects, see the demo for more complete usage
- `onLayoutChange` (optional): The callback that is fired when the layout changes
- `rowHeight` (optional): The row height of the grid
- `setProps` (optional): Dash-assigned callback that should be called whenever any of the
properties change
"""
function ''_grid(; kwargs...)
        available_props = Symbol[:children, :id, :cols, :isDraggable, :isResizable, :layout, :onLayoutChange, :rowHeight]
        wild_props = Symbol[]
        return Component("''_grid", "Grid", "dash_grid_layout", available_props, wild_props; kwargs...)
end

''_grid(children::Any; kwargs...) = ''_grid(;kwargs..., children = children)
''_grid(children_maker::Function; kwargs...) = ''_grid(children_maker(); kwargs...)

