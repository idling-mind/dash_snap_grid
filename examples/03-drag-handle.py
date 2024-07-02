import dash_mantine_components as dmc
from dash_snap_grid import Grid
from random import randint
from dash import Dash, dcc

TITLE = "Drag Handle"
DESCRIPTION = """
This example shows how you can use one or more elements as a drag handle for the grid items.
Use the `.drag-handle` class to specify the drag handle element. In this example, the title
of the card is used as the drag handle.
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
                style={"cursor": "move", "background": "aliceblue"},
                className="drag-handle",
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
                dcc.Markdown(DESCRIPTION),
                Grid(
                    id="grid",
                    cols=12,
                    rowHeight=100,
                    layout=initial_layout,
                    draggableHandle=".drag-handle",
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


if __name__ == "__main__":
    app.run(debug=True)