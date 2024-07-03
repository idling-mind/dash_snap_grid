import dash_mantine_components as dmc
from dash_snap_grid import Grid, DraggableDiv
from random import randint
from dash import Dash, html, Output, Input, State, dcc

TITLE = "Drag and drop example"
DESCRIPTION = """
This example shows how to make the Grid droppable and how to use the DraggableDiv component.
The DraggableDiv component is a wrapper around `html.Div` with `draggable` attribute
and `ondragstart` event handler. It allows to drag the div and drop it into the Grid.

Once dropped, the Grid's `droppedItem` prop will update to the layout information
of the dropped item. The layout information is a dictionary with the following keys:
* `i` - The id of the dropped item
* `x` - x position
* `y` - y position
* `w` - width
* `h` - height
"""

app = Dash(__name__)


def card(id, title, text, layout, color="blue"):
    return dmc.Card(
        id=id,
        children=[
            dmc.CardSection(
                dmc.Text(title, size="xl", fw=500, c="white"),
                withBorder=True,
                p=10,
                bg=color,
            ),
            dmc.Text(
                text,
                size="sm",
                c="dimmed",
            ),
            dmc.Code(str(layout)),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        h="100%",
    )


initial_layout = [
    {
        "i": f"item-{x}",
        "x": x * 3 % 12,
        "y": 0,
        "w": 3,
        "h": randint(2, 3),
    }
    for x in range(3)
]

app.layout = dmc.MantineProvider(
    [
        dmc.Stack(
            [
                dmc.Title(TITLE, order=2),
                dcc.Markdown(DESCRIPTION),
                dmc.Paper(
                    dmc.Group(
                        [
                            DraggableDiv(dmc.Button("Drag me!"), id="drag-blue"),
                            DraggableDiv(
                                dmc.Button("Or me!", color="green"), id="drag-green"
                            ),
                        ]
                    ),
                    p=20,
                    shadow="sm",
                    withBorder=True,
                ),
                Grid(
                    id="grid",
                    cols=12,
                    rowHeight=100,
                    layout=initial_layout,
                    isDroppable=True,
                    children=[
                        card(
                            item["i"],
                            f"Card {item['i']} title",
                            f"This card is at position {item['x']}, {item['y']}"
                            f" with width {item['w']} and height {item['h']}",
                            item,
                        )
                        for item in initial_layout
                    ],
                ),
            ],
            p=20,
        ),
    ]
)


@app.callback(
    Output("grid", "children"),
    Output("grid", "layout"),
    Input("grid", "droppedItem"),
    State("grid", "children"),
    State("grid", "layout"),
)
def update_children(dropped_item, children, layout):
    if not dropped_item:
        return children, layout

    # Modify the dropped item to suit the need
    if dropped_item["i"] == "drag-blue":
        color = "blue"
    elif dropped_item["i"] == "drag-green":
        color = "limegreen"
    dropped_item["i"] = f"item-{len(layout)}"
    dropped_item["w"] = 2
    dropped_item["h"] = 2

    new_item = card(
        dropped_item["i"],
        f"Card {dropped_item['i']} title",
        f"This card is at position {dropped_item['x']}, {dropped_item['y']}"
        f" with width {dropped_item['w']} and height {dropped_item['h']}",
        dropped_item,
        color=color,
    )

    return children + [new_item], layout + [dropped_item]


if __name__ == "__main__":
    app.run(debug=True)