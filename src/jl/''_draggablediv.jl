# AUTO GENERATED FILE - DO NOT EDIT

export ''_draggablediv

"""
    ''_draggablediv(;kwargs...)
    ''_draggablediv(children::Any;kwargs...)
    ''_draggablediv(children_maker::Function;kwargs...)


A DraggableDiv component.

Keyword arguments:
- `children` (optional): The children of this component
- `id` (optional): The ID of this component, used to identify dash components in callbacks
- `setProps` (optional): Dash-assigned callback that gets fired when the input changes.
This callback will have the new value.
- `style` (optional): The style of this component
"""
function ''_draggablediv(; kwargs...)
        available_props = Symbol[:children, :id, :style]
        wild_props = Symbol[]
        return Component("''_draggablediv", "DraggableDiv", "dash_snap_grid", available_props, wild_props; kwargs...)
end

''_draggablediv(children::Any; kwargs...) = ''_draggablediv(;kwargs..., children = children)
''_draggablediv(children_maker::Function; kwargs...) = ''_draggablediv(children_maker(); kwargs...)

