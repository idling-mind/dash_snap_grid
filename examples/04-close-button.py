import dash_mantine_components as dmc
from dash_snap_grid import Grid
from random import randint
from dash import Dash, ALL, Input, Output, State, ctx
from dash_iconify import DashIconify

TITLE = "Close button example"
DESCRIPTION = """
This example shows a couple of interesting concepts. How to disable dragging on
specific elements and how to remove a card from the grid using a close button.

The `draggableCancel` prop in the `Grid` component is used to disable dragging on
the close button. The close button is a `ActionIcon` component with the `no-drag`
class. This class is used to disable dragging on the close button.

A callback is used to remove the card from the grid when the close button is clicked.
The `close_card` callback is triggered by the `n_clicks` prop of the close button.
The `ctx.triggered_id` is used to get the index of the card that was clicked.
The card is removed from the grid by filtering the children of the grid and
excluding the card that was clicked.
"""


app = Dash(__name__)


def card(id, title, text, layout):
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
    for x in range(4)
]

app.layout = dmc.MantineProvider(
    [
        dmc.Stack(
            [
                dmc.Title(TITLE, order=2),
                dmc.Text(DESCRIPTION),
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
    Input({"type": "close", "index": ALL}, "n_clicks"),
    State("grid", "children"),
    prevent_initial_call=True,
)
def close_card(clicks, children):
    if clicks is None:
        return children
    index = ctx.triggered_id["index"]
    return [child for child in children if child["props"]["id"] != index]


if __name__ == "__main__":
    app.run(debug=True)