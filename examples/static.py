import dash_mantine_components as dmc
from dash_snap_grid import Grid
from random import randint
from dash import Dash, html


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
        "x": x * 3 % 12,
        "y": 0,
        "w": 3,
        "h": randint(2, 3),
    }
    for x in range(10)
]

app.layout = dmc.MantineProvider(
    [
        dmc.Stack(
            [
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
                )
            ]
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)