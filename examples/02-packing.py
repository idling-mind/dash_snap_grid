import dash_mantine_components as dmc
from dash_snap_grid import Grid
from random import randint
from dash import Dash, callback, Input, Output

TITLE = "Packing direction"
DESCRIPTION = """
This is an example showing the different packing directions of the grid.
Choose a direction from the radio buttons below to see the effect.

Note that once you change the direction, the grid will be re-packed which causes
the layout to be changed permanently. Changing the direction back to what it was
before will not have any effect as the grid will be packed in the new direction.
"""

app = Dash(__name__)


def card(id, title, text, layout):
    return dmc.Card(
        id=id,
        children=[
            dmc.Text(title, fw=500),
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
        "x": randint(0, 10),
        "y": randint(0, 10),
        "w": 2,
        "h": randint(2, 3),
    }
    for x in range(10)
]

app.layout = dmc.MantineProvider(
    [
        dmc.Stack(
            [
                dmc.Title(TITLE, order=2),
                dmc.Text(DESCRIPTION),
                dmc.Group(
                    [
                        dmc.RadioGroup(
                            children=dmc.Group(
                                [
                                    dmc.Radio("None", value="null"),
                                    dmc.Radio("Horizontal", value="horizontal"),
                                    dmc.Radio("Vertical", value="vertical"),
                                ],
                                my=10,
                            ),
                            id="direction",
                            value="null",
                            label="Select the packing direction",
                        ),
                    ],
                ),
                Grid(
                    id="grid",
                    cols=12,
                    rowHeight=100,
                    layout=initial_layout,
                    isDraggable=False,
                    isResizable=False,
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
            p=10,
        ),
    ]
)


@callback(
    Output("grid", "compactType"),
    Input("direction", "value"),
)
def change_compact_type(value):
    if value == "null":
        return None
    return value


if __name__ == "__main__":
    app.run(debug=True)