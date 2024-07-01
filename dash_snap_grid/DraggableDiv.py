# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DraggableDiv(Component):
    """A DraggableDiv component.


Keyword arguments:

- children (optional):
    The children of this component.

- id (optional):
    The ID of this component, used to identify dash components in
    callbacks.

- setProps (optional):
    Dash-assigned callback that gets fired when the input changes.
    This callback will have the new value.

- style (optional):
    The style of this component."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_snap_grid'
    _type = 'DraggableDiv'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'setProps', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'setProps', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DraggableDiv, self).__init__(children=children, **args)
