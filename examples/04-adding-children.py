import dash_mantine_components as dmc
from dash_snap_grid import Grid
from random import randint
from dash import Dash, ALL, Input, Output, State, ctx, dcc
from dash_iconify import DashIconify

TITLE = "Add children example"
DESCRIPTION = """
This example shows how to add children to the grid using a callback.
The children are added at the bottom of the grid by setting the `y` value to a high number.
The `compactType` prop of the `Grid` component is set to `vertical` to make the grid
compact vertically. This is necessary to add children at the bottom of the grid.

The x, y, w, and h values of the new card are randomly generated. The new card is
appended to the `children` and `layout` props of the `Grid` component.
"""


app = Dash(__name__)


def card(id, title, text, layout):
    return dmc.Card(
        id=id,
        children=[
            dmc.CardSection(
                dmc.Text(title, fw=500, size="xl"),
                withBorder=True,
                p=10,
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
    for x in range(2)
]

app.layout = dmc.MantineProvider(
    [
        dmc.Stack(
            [
                dmc.Title(TITLE, order=2),
                dcc.Markdown(DESCRIPTION),
                dmc.Button("Add card", id="add-card", size="lg", variant="outline"),
                Grid(
                    id="grid",
                    cols=12,
                    rowHeight=100,
                    layout=initial_layout,
                    compactType="vertical",
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
    Input("add-card", "n_clicks"),
    State("grid", "children"),
    State("grid", "layout"),
    prevent_initial_call=True,
)
def add_card(clicks, children, layout):
    new_card = {
        "i": f"item-{len(children)}",
        "x": randint(0, 9),
        "y": 1000,  # This is the trick to add a new card at the bottom (only works with vertical compactType)
        "w": randint(2, 4),
        "h": randint(2, 4),
    }
    layout.append(new_card)
    children.append(
        card(
            new_card["i"],
            f"Card {new_card['i']} title",
            f"This card is at position {new_card['x']}, {new_card['y']}"
            f" with width {new_card['w']} and height {new_card['h']}",
            new_card,
        )
    )
    return children, layout


if __name__ == "__main__":
    app.run(debug=True)