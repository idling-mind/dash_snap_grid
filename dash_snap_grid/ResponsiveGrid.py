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


class ResponsiveGrid(Component):
    """A ResponsiveGrid component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of the grid.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- allowOverlap (boolean; default False):
    allow overlapping in the grid.

- autoSize (boolean; default True):
    If True, container size swells to fit contents.

- breakpoint (string; optional):
    The current breakpoint.

- breakpoints (dict; default { lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0 }):
    breakpoints for responsive design.

- col (number; optional):
    The current column count.

- cols (dict; default { lg: 12, md: 10, sm: 6, xs: 4, xxs: 2 }):
    The number of columns in the grid. This is an object with keys lg,
    md, sm, xs, xxs.

- compactType (a value equal to: 'vertical', 'horizontal', null; optional):
    Compaction type.

- containerPadding (default [10, 10]):
    Padding inside the container [x, y] in px. Can be an object with
    keys lg, md, sm, xs, xxs  and values [x, y].

- draggableCancel (string; optional):
    A CSS selector for tags that will not be draggable  Use this to so
    that some elements like buttons register clicks as expected.

- draggableHandle (string; optional):
    A CSS selector for tags that will act as the draggable handle.

- droppedItem (dict; optional):
    ID of the dropped element.

- isBounded (boolean; default False):
    Is bounded.

- isDraggable (boolean; default True):
    Whether the grid items are draggable.

- isDroppable (boolean; default False):
    if True, droppable elements (with draggable=True) can be dropped
    on the grid  droppedItem is the layout information of the dropped
    element.

- isResizable (boolean; default True):
    Whether the grid items are resizable.

- layout (list of dicts; optional):
    The layout of the grid, Readonly.

- layouts (dict; optional):
    The layouts of the grid.

- margin (default [10, 10]):
    Margin between items [x, y] in px. Can be an object with keys lg,
    md, sm, xs, xxs  and values [x, y].

- preventCollision (boolean; default False):
    If True, grid items wont change position when being dragged over.

- resizeHandles (list of strings; default ['se']):
    Which resize handles to display  s, e, w, n, se, ne, sw, nw.

- rowHeight (number; default 150):
    The row height of the grid. Default is 150.

- transformScale (number; default 1):
    If parent DOM node of ResponsiveReactGridLayout or ReactGridLayout
    has \"transform: scale(n)\" css property,  we should set scale
    coefficient to avoid render artefacts while dragging.

- useCSSTransforms (boolean; default True):
    Uses CSS3 `translate()` instead of position top/left.  This makes
    about 6x faster paint performance.

- width (number; optional):
    Initial width of the grid."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_snap_grid'
    _type = 'ResponsiveGrid'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        width: typing.Optional[NumberType] = None,
        autoSize: typing.Optional[bool] = None,
        cols: typing.Optional[dict] = None,
        col: typing.Optional[NumberType] = None,
        draggableCancel: typing.Optional[str] = None,
        draggableHandle: typing.Optional[str] = None,
        compactType: typing.Optional[Literal["vertical", "horizontal", None]] = None,
        layout: typing.Optional[typing.Sequence[dict]] = None,
        layouts: typing.Optional[dict] = None,
        margin: typing.Optional[typing.Any] = None,
        containerPadding: typing.Optional[typing.Any] = None,
        rowHeight: typing.Optional[NumberType] = None,
        isDraggable: typing.Optional[bool] = None,
        isResizable: typing.Optional[bool] = None,
        isBounded: typing.Optional[bool] = None,
        useCSSTransforms: typing.Optional[bool] = None,
        transformScale: typing.Optional[NumberType] = None,
        allowOverlap: typing.Optional[bool] = None,
        preventCollision: typing.Optional[bool] = None,
        isDroppable: typing.Optional[bool] = None,
        droppedItem: typing.Optional[dict] = None,
        resizeHandles: typing.Optional[typing.Sequence[str]] = None,
        breakpoints: typing.Optional[dict] = None,
        breakpoint: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'allowOverlap', 'autoSize', 'breakpoint', 'breakpoints', 'col', 'cols', 'compactType', 'containerPadding', 'draggableCancel', 'draggableHandle', 'droppedItem', 'isBounded', 'isDraggable', 'isDroppable', 'isResizable', 'layout', 'layouts', 'margin', 'preventCollision', 'resizeHandles', 'rowHeight', 'transformScale', 'useCSSTransforms', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'allowOverlap', 'autoSize', 'breakpoint', 'breakpoints', 'col', 'cols', 'compactType', 'containerPadding', 'draggableCancel', 'draggableHandle', 'droppedItem', 'isBounded', 'isDraggable', 'isDroppable', 'isResizable', 'layout', 'layouts', 'margin', 'preventCollision', 'resizeHandles', 'rowHeight', 'transformScale', 'useCSSTransforms', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ResponsiveGrid, self).__init__(children=children, **args)

setattr(ResponsiveGrid, "__init__", _explicitize_args(ResponsiveGrid.__init__))
