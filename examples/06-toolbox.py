import dash_mantine_components as dmc
from dash_snap_grid import Grid
from random import randint
from dash import Dash, ALL, Input, Output, State, ctx, dcc
from dash_iconify import DashIconify

TITLE = "Close button example"
DESCRIPTION = """
This example shows a couple of interesting concepts. How to disable dragging on
specific elements and how to remove a card from the grid using a close button.

The `draggableCancel` prop in the `Grid` component is used to disable dragging on
the close button. The close button is a `ActionIcon` component with the `no-drag`
class. This class is used to disable dragging on the close button.

A callback is used to remove the card from the grid when the close button is clicked.
And it is added to the toolbox when the card is removed. The removed card is added
to the store to keep track of the removed children. A button is added to the toolbox
for each removed card. When the button is clicked, the card is added back to the grid.

The initial layout is set back everytime there is change in the grid children.
So, even if you re-arrange the cards between closing and adding back, they will
go back to their initial positions. This could be changed by saving the layout
every time there is a change in the layout prop.
"""


app = Dash(__name__)


def card(id, title, text):
    return dmc.Card(
        id=id,
        children=[
            dmc.CardSection(
                dmc.Group(
                    [
                        dmc.Text(title, fw=500, size="xl"),
                        dmc.ActionIcon(
                            DashIconify(icon="mdi:close"),
                            id={"type": "close", "index": id},
                            size="sm",
                            radius="xl",
                            variant="outline",
                            className="no-drag",
                        ),
                    ],
                    justify="space-between",
                ),
                withBorder=True,
                p=10,
                style={"background": "aliceblue"},
            ),
            dmc.Text(
                text,
                size="sm",
                c="dimmed",
            ),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        h="100%",
    )


initial_layout = [
    {
        "i": f"item-{x}",
        "x": x * 2 % 12,
        "y": 0,
        "w": 2,
        "h": randint(2, 3),
    }
    for x in range(8)
]

app.layout = dmc.MantineProvider(
    [
        dmc.Stack(
            [
                dmc.Title(TITLE, order=2),
                dcc.Markdown(DESCRIPTION),
                dmc.Paper(
                    dmc.Group(id="toolbox"),
                    p=20,
                    c="gray-1",
                    radius="md",
                    shadow="xs",
                    withBorder=True,
                    h="150px",
                ),
                dcc.Store(id="store-toolbox", data=[]),
                Grid(
                    id="grid",
                    cols=12,
                    rowHeight=100,
                    layout=initial_layout,
                    draggableCancel=".no-drag",
                    children=[
                        card(
                            item["i"],
                            f"Card {item['i']} title",
                            f"This card is at position {item['x']}, {item['y']}"
                            f" with width {item['w']} and height {item['h']}",
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
    Output("store-toolbox", "data"),
    Output("toolbox", "children"),
    Output("grid", "layout"),
    Input({"type": "close", "index": ALL}, "n_clicks"),
    Input({"type": "toolbox-icon", "index": ALL}, "n_clicks"),
    State("grid", "children"),
    State("store-toolbox", "data"),
    prevent_initial_call=True,
)
def close_card(clicks_close, clicks_icon, children, toolbox):
    if ctx.triggered_id["type"] == "close":
        index = ctx.triggered_id["index"]
        new_children = [child for child in children if child["props"]["id"] != index]
        toolbox_store = toolbox + [
            child for child in children if child["props"]["id"] == index
        ]
        toolbox_children = [
            dmc.Button(
                x["props"]["id"],
                id={"type": "toolbox-icon", "index": x["props"]["id"]},
                size="sm",
            )
            for x in toolbox_store
        ]
    elif ctx.triggered_id["type"] == "toolbox-icon":
        index = ctx.triggered_id["index"]
        new_children = children + [
            child for child in toolbox if child["props"]["id"] == index
        ]
        toolbox_store = [child for child in toolbox if child["props"]["id"] != index]
        toolbox_children = [
            dmc.Button(
                x["props"]["id"],
                id={"type": "toolbox-icon", "index": x["props"]["id"]},
                size="sm",
            )
            for x in toolbox_store
        ]
    return new_children, toolbox_store, toolbox_children, initial_layout


if __name__ == "__main__":
    app.run(debug=True)