# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GridItem(Component):
    """A GridItem component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of the grid.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- bounded (boolean; optional):
    Whether the grid item is bounded within the grid container.

- draggable (boolean; optional):
    Whether the grid item is draggable.

- height (number; optional):
    The height of the grid item.

- max_height (number; optional):
    The maximum height of the grid item.

- max_width (number; optional):
    The maximum width of the grid item.

- min_height (number; optional):
    The minimum height of the grid item.

- min_width (number; optional):
    The minimum width of the grid item.

- resizable (boolean; optional):
    Whether the grid item is resizable.

- static (boolean; optional):
    Whether the grid item is static (non-draggable and non-resizable).

- style (dict; optional):
    The style of the grid item.

- width (number; optional):
    The width of the grid item.

- x (number; optional):
    The x position of the grid item.

- y (number; optional):
    The y position of the grid item."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_grid_layout'
    _type = 'GridItem'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, x=Component.UNDEFINED, y=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, static=Component.UNDEFINED, min_width=Component.UNDEFINED, min_height=Component.UNDEFINED, max_width=Component.UNDEFINED, max_height=Component.UNDEFINED, draggable=Component.UNDEFINED, resizable=Component.UNDEFINED, bounded=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bounded', 'draggable', 'height', 'max_height', 'max_width', 'min_height', 'min_width', 'resizable', 'static', 'style', 'width', 'x', 'y']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bounded', 'draggable', 'height', 'max_height', 'max_width', 'min_height', 'min_width', 'resizable', 'static', 'style', 'width', 'x', 'y']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(GridItem, self).__init__(children=children, **args)
