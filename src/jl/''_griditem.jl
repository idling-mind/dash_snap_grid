# AUTO GENERATED FILE - DO NOT EDIT

export ''_griditem

"""
    ''_griditem(;kwargs...)
    ''_griditem(children::Any;kwargs...)
    ''_griditem(children_maker::Function;kwargs...)


A GridItem component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The children of the grid
- `id` (String; optional): The ID used to identify this component in Dash callbacks
- `bounded` (Bool; optional): Whether the grid item is bounded within the grid container
- `draggable` (Bool; optional): Whether the grid item is draggable
- `height` (Real; optional): The height of the grid item
- `max_height` (Real; optional): The maximum height of the grid item
- `max_width` (Real; optional): The maximum width of the grid item
- `min_height` (Real; optional): The minimum height of the grid item
- `min_width` (Real; optional): The minimum width of the grid item
- `resizable` (Bool; optional): Whether the grid item is resizable
- `static` (Bool; optional): Whether the grid item is static (non-draggable and non-resizable)
- `style` (Dict; optional): The style of the grid item
- `width` (Real; optional): The width of the grid item
- `x` (Real; optional): The x position of the grid item
- `y` (Real; optional): The y position of the grid item
"""
function ''_griditem(; kwargs...)
        available_props = Symbol[:children, :id, :bounded, :draggable, :height, :max_height, :max_width, :min_height, :min_width, :resizable, :static, :style, :width, :x, :y]
        wild_props = Symbol[]
        return Component("''_griditem", "GridItem", "dash_grid_layout", available_props, wild_props; kwargs...)
end

''_griditem(children::Any; kwargs...) = ''_griditem(;kwargs..., children = children)
''_griditem(children_maker::Function; kwargs...) = ''_griditem(children_maker(); kwargs...)

