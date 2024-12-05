# dash-snap-grid

A draggable and resizable grid layout with responsive breakpoints, for Dash.

(A dash port of [react-grid-layout](https://github.com/react-grid-layout/react-grid-layout)
with some additional features specific to Dash)

![dash-grid-layout](./demo.gif)


## Installation

```bash
pip install dash-snap-grid
```

## Basic Usage

You must set the env variable `REACT_VERSION=18.2.0` before starting up the app.

```python
import dash
from dash import html
from dash_snap_grid import Grid

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        Grid(
            id="grid",
            cols=12,
            rowHeight=100,
            layout=[
                # i should match the id of the children
                {"i": "1", "x": 0, "y": 0, "w": 1, "h": 2},
                {"i": "2", "x": 1, "y": 0, "w": 3, "h": 2},
                {"i": "3", "x": 4, "y": 0, "w": 1, "h": 2},
            ],
            children=[
                html.Div(
                    "1", id="1", style={"background": "lightblue", "height": "100%"}
                ),
                html.Div(
                    "2", id="2", style={"background": "lightgreen", "height": "100%"}
                ),
                html.Div(
                    "3", id="3", style={"background": "lightcoral", "height": "100%"}
                ),
            ],
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

```

## Components

### Grid

The main component that wraps the children and handles the layout.

#### Props

- `id` (str): The id of the component.
- `width` (int): The initial width of the grid.
- `autoSize` (bool): If true, the grid will automatically resize to fit the children. (default: True)
- `cols` (int): The number of columns in the grid. (default: 12)
- `draggableCancel` (str): A css selector for elements that should not trigger drag.
  Use this if you have input elements or buttons inside the grid.
- `draggableHandle` (str): A css selector for elements that should be used as the drag handle.
- `compactType` (str | None): The type of compacting to use when moving elements around.
  Options: None, `vertical`, `horizontal`. (default: None)
- `layout` (List[Dict[str, Any]]): The initial layout of the grid.
  Each item should have the following keys:
  - `i` (str): The id of the child.
  - `x` (int): The x position of the child.
  - `y` (int): The y position of the child.
  - `w` (int): The width of the child. (count of columns)
  - `h` (int): The height of the child. (count of rows)
  The following keys are optional:
  - `minW` (int): The minimum width of the child. (default: 0)
  - `maxW` (int): The maximum width of the child. (default: Infinity)
  - `minH` (int): The minimum height of the child. (default: 0)
  - `maxH` (int): The maximum height of the child. (default: Infinity)
  - `static` (bool): If true, the child cannot be moved or resized. (default: False)
  - `isDraggable` (bool): If false, the child cannot be dragged. (default: True)
  - `isResizable` (bool): If false, the child cannot be resized. (default: True)
  - `isBounded` (bool): If true, the child will be bounded by the grid. (default: False)
- `persistLayout` (bool): If true, any changes to the layout will be stored in browser storage.
  Reloading the page will restore the last layout update that the user did.
- `margin` (List[int]): The margin between the children. (default: [10, 10])
- `containerPadding` (List[int]): The padding of the container. (default: [10, 10])
- `rowHeight` (int): The height of a row in pixels. (default: 150)
- `isDraggable` (bool): If true, the children can be dragged. (default: True)
- `isResizable` (bool): If true, the children can be resized. (default: True)
- `isBounded` (bool): If true, the children will be bounded by the grid. (default: False)
- `useCSSTransforms` (bool): If true, the children will be moved using css transforms. (default: True)
- `transformScale` (float): The scale of the transform. (default: 1)
- `allowOverlap` (bool): If true, the children can overlap. (default: False)
- `preventCollision` (bool): If true, the children will not collide with each other. (default: False)
- `isDroppable` (bool): If true, the children can be dropped. (default: False).
  Once an item is dropped, the `droppedItem` prop will be updated with the layout details
  of the dropped item, which contains the the layout details of the dropped item.
  the `i` key will be set to the id of the dropped item.
- `resizeHandles` (List[str]): The handles that can be used to resize the children.
  Options: `['s', 'e', 'n', 'w', 'se', 'ne', 'sw', 'nw']`. (default: ['se'])
- `children` (List[html.Div]): The children of the grid. Make sure the id of the children
  matches the `i` key of the layout items.

### ResponsiveGrid

A responsive version of the grid that changes the layout based on the screen size.

#### Props

- `id` (str): The id of the component.
- `width` (int): The initial width of the grid.
- `autoSize` (bool): If true, the grid will automatically resize to fit the children. (default: True)
- `breakpoints` (Dict[str, int]): The breakpoints for the grid. The keys should be the screen sizes
  and the values should be the number of columns in the grid for that screen size.
  default: `{'lg': 1200, 'md': 996, 'sm': 768, 'xs': 400, 'xxs': 0}`
- `cols` (dict[str, int]): Number of columns per screen size. The keys should be the screen sizes
  and the values should be the number of columns in the grid for that screen size.
  default: `{'lg': 12, 'md': 10, 'sm': 6, 'xs': 4, 'xxs': 2}`
- `draggableCancel` (str): A css selector for elements that should not trigger drag.
  Use this if you have input elements or buttons inside the grid.
- `draggableHandle` (str): A css selector for elements that should be used as the drag handle.
- `compactType` (str | None): The type of compacting to use when moving elements around.
  Options: None, `vertical`, `horizontal`. (default: None)
- `layout` (List[Dict[str, Any]]): The current layout (Read only)
  Each item should have the following keys:
  - `i` (str): The id of the child.
  - `x` (int): The x position of the child.
  - `y` (int): The y position of the child.
  - `w` (int): The width of the child. (count of columns)
  - `h` (int): The height of the child. (count of rows)
  The following keys are optional:
  - `minW` (int): The minimum width of the child. (default: 0)
  - `maxW` (int): The maximum width of the child. (default: Infinity)
  - `minH` (int): The minimum height of the child. (default: 0)
  - `maxH` (int): The maximum height of the child. (default: Infinity)
  - `static` (bool): If true, the child cannot be moved or resized. (default: False)
  - `isDraggable` (bool): If false, the child cannot be dragged. (default: True)
  - `isResizable` (bool): If false, the child cannot be resized. (default: True)
  - `isBounded` (bool): If true, the child will be bounded by the grid. (default: False)
- `layouts` (Dict[str, List[Dict[str, Any]]]): The initial layout of the grid for each screen size.
  This is dictionary of layouts, where the keys are the screen sizes and the values are the layouts.
  If you want to set the layout for a given screen size, this prop should be set. `layout` prop is only
  to read the current layout.
  for example: `{'lg': [...], 'md': [...], 'sm': [...], 'xs': [...], 'xxs': [...]}`.
- `persistLayout` (bool): If true, any changes to the layout will be stored in browser storage.
  The layout change made at each breakpoint will be saved separately. So layout presistance will happen
  at each breakpoint.
- `margin` (List[int] | dict[str, int]): The margin between the children. (default: [10, 10])
  You can also specify the margin for each screen size by passing a dictionary.
  for example: `{'lg': [10, 10], 'md': [5, 5], 'sm': [2, 2], 'xs': [1, 1], 'xxs': [0, 0]}`
- `containerPadding` (List[int] | dict[str, int]): The padding of the container. (default: [10, 10])
  Similar to the margin, you can also specify the padding for each screen size by passing a dictionary.
- `rowHeight` (int): The height of a row in pixels. (default: 150)
- `isDraggable` (bool): If true, the children can be dragged. (default: True)
- `isResizable` (bool): If true, the children can be resized. (default: True)
- `isBounded` (bool): If true, the children will be bounded by the grid. (default: False)
- `useCSSTransforms` (bool): If true, the children will be moved using css transforms. (default: True)
- `transformScale` (float): The scale of the transform. (default: 1)
- `allowOverlap` (bool): If true, the children can overlap. (default: False)
- `preventCollision` (bool): If true, the children will not collide with each other. (default: False)
- `isDroppable` (bool): If true, the children can be dropped. (default: False).
  Once an item is dropped, the `droppedItem` prop will be updated with the layout details
  of the dropped item, which contains the the layout details of the dropped item.
  the `i` key will be set to the id of the dropped item.
- `resizeHandles` (List[str]): The handles that can be used to resize the children.
  Options: `['s', 'e', 'n', 'w', 'se', 'ne', 'sw', 'nw']`. (default: ['se'])
- `children` (List[html.Div]): The children of the grid. Make sure the id of the children
  matches the `i` key of the layout items.

### DraggableDiv

A draggable div that can be used as a an item that can be dragged and dropped in the grid.

#### Props

- `id` (str): The id of the component.
- `children` (html.Div): The children of the div.
- `style` (dict): The style of the div.