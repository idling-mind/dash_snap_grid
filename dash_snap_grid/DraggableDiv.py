# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


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
    This callback will have the new value."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_snap_grid'
    _type = 'DraggableDiv'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        style: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'setProps', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'setProps', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DraggableDiv, self).__init__(children=children, **args)

setattr(DraggableDiv, "__init__", _explicitize_args(DraggableDiv.__init__))
