import dash_mantine_components as dmc
from dash_snap_grid import ResponsiveGrid
from random import randint
from dash import Dash, html, callback, Input, Output, State

TITLE = "Basic Example"
DESCRIPTION = """
This is a simple example of how to use the `dash_snap_grid` component with `dash_mantine_components`.
Try dragging the cards around to see how they snap to the grid. Also try resizing them.
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
                dmc.Title(TITLE, order=2),
                dmc.Text(DESCRIPTION),
                dmc.Code(id="breakpoint"),
                ResponsiveGrid(
                    id="grid",
                    cols={"lg": 12, "md": 10, "sm": 6, "xs": 4, "xxs": 2},
                    breakpoints={"lg": 1200, "md": 996, "sm": 768, "xs": 480, "xxs": 0},
                    rowHeight=100,
                    layouts={"lg":initial_layout},
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

@callback(
    Output("breakpoint", "children"),
    Input("grid", "breakpoint"),
    State("grid", "col"),
)
def change_layout(breakpoint, col):
    return f"Current breakpoint: {breakpoint}, Current column: {col}"

if __name__ == "__main__":
    app.run(debug=True)