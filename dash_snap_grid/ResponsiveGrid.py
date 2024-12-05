# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ResponsiveGrid(Component):
    """A ResponsiveGrid component.


Keyword arguments:

- children (optional):
    The children of the grid.

- id (optional):
    The ID used to identify this component in Dash callbacks.

- allowOverlap (default False):
    allow overlapping in the grid.

- autoSize (default True):
    If True, container size swells to fit contents.

- breakpoints (default {lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0}):
    breakpoints for responsive design.

- cols (default {lg: 12, md: 10, sm: 6, xs: 4, xxs: 2}):
    The number of columns in the grid. This is an object with keys lg,
    md, sm, xs, xxs.

- compactType (optional):
    Compaction type.

- containerPadding (default [10, 10]):
    Padding inside the container [x, y] in px. Can be an object with
    keys lg, md, sm, xs, xxs  and values [x, y].

- draggableCancel (optional):
    A CSS selector for tags that will not be draggable  Use this to so
    that some elements like buttons register clicks as expected.

- draggableHandle (optional):
    A CSS selector for tags that will act as the draggable handle.

- droppedItem (optional):
    ID of the dropped element.

- isBounded (default False):
    Is bounded.

- isDraggable (default True):
    Whether the grid items are draggable.

- isDroppable (default False):
    if True, droppable elements (with draggable=True) can be dropped
    on the grid  droppedItem is the layout information of the dropped
    element.

- isResizable (default True):
    Whether the grid items are resizable.

- layout (optional):
    The layout of the grid, Readonly.

- layouts (optional):
    The layouts of the grid.

- margin (default [10, 10]):
    Margin between items [x, y] in px. Can be an object with keys lg,
    md, sm, xs, xxs  and values [x, y].

- persistLayout (optional):
    The persistance of the layouts. If True, layouts are saved to
    local storage  and will be used when the component is loaded after
    pageload or refresh.  Layouts at all breakpoints are saved to the
    same key.

- preventCollision (default False):
    If True, grid items wont change position when being dragged over.

- resizeHandles (default ['se']):
    Which resize handles to display  s, e, w, n, se, ne, sw, nw.

- rowHeight (default 150):
    The row height of the grid. Default is 150.

- setProps (optional):
    Dash-assigned callback that should be called whenever any of the
    properties change.

- transformScale (default 1):
    If parent DOM node of ResponsiveReactGridLayout or ReactGridLayout
    has \"transform: scale(n)\" css property,  we should set scale
    coefficient to avoid render artefacts while dragging.

- useCSSTransforms (default True):
    Uses CSS3 `translate()` instead of position top/left.  This makes
    about 6x faster paint performance.

- width (optional):
    Initial width of the grid."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_snap_grid'
    _type = 'ResponsiveGrid'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, width=Component.UNDEFINED, autoSize=Component.UNDEFINED, cols=Component.UNDEFINED, draggableCancel=Component.UNDEFINED, draggableHandle=Component.UNDEFINED, compactType=Component.UNDEFINED, layout=Component.UNDEFINED, layouts=Component.UNDEFINED, margin=Component.UNDEFINED, containerPadding=Component.UNDEFINED, rowHeight=Component.UNDEFINED, isDraggable=Component.UNDEFINED, isResizable=Component.UNDEFINED, isBounded=Component.UNDEFINED, useCSSTransforms=Component.UNDEFINED, transformScale=Component.UNDEFINED, allowOverlap=Component.UNDEFINED, preventCollision=Component.UNDEFINED, isDroppable=Component.UNDEFINED, droppedItem=Component.UNDEFINED, resizeHandles=Component.UNDEFINED, breakpoints=Component.UNDEFINED, persistLayout=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'allowOverlap', 'autoSize', 'breakpoints', 'cols', 'compactType', 'containerPadding', 'draggableCancel', 'draggableHandle', 'droppedItem', 'isBounded', 'isDraggable', 'isDroppable', 'isResizable', 'layout', 'layouts', 'margin', 'persistLayout', 'preventCollision', 'resizeHandles', 'rowHeight', 'setProps', 'transformScale', 'useCSSTransforms', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'allowOverlap', 'autoSize', 'breakpoints', 'cols', 'compactType', 'containerPadding', 'draggableCancel', 'draggableHandle', 'droppedItem', 'isBounded', 'isDraggable', 'isDroppable', 'isResizable', 'layout', 'layouts', 'margin', 'persistLayout', 'preventCollision', 'resizeHandles', 'rowHeight', 'setProps', 'transformScale', 'useCSSTransforms', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ResponsiveGrid, self).__init__(children=children, **args)
