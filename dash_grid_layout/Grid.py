# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Grid(Component):
    """A Grid component.


Keyword arguments:

- children (optional):
    The children of the grid.

- id (optional):
    The ID used to identify this component in Dash callbacks.

- cols (default 12):
    The number of columns in the grid.

- isDraggable (default True):
    Whether the grid items are draggable.

- isResizable (default True):
    Whether the grid items are resizable.

- layout (optional):
    The layout of the grid  This is an array of objects, see the demo
    for more complete usage.

- onLayoutChange (optional):
    The callback that is fired when the layout changes.

- rowHeight (default 30):
    The row height of the grid.

- setProps (optional):
    Dash-assigned callback that should be called whenever any of the
    properties change."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_grid_layout'
    _type = 'Grid'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, cols=Component.UNDEFINED, rowHeight=Component.UNDEFINED, layout=Component.UNDEFINED, isDraggable=Component.UNDEFINED, isResizable=Component.UNDEFINED, onLayoutChange=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'cols', 'isDraggable', 'isResizable', 'layout', 'onLayoutChange', 'rowHeight', 'setProps']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'cols', 'isDraggable', 'isResizable', 'layout', 'onLayoutChange', 'rowHeight', 'setProps']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Grid, self).__init__(children=children, **args)
