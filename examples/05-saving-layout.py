import dash_mantine_components as dmc
from dash_snap_grid import Grid
from random import randint
from dash import Dash, ALL, Input, Output, State, ctx, dcc, no_update
from pprint import pformat

TITLE = "Saving layout"
DESCRIPTION = """
This example shows how to save the current layout of the grid. The layout of the grid
is stored in the `layout` prop of the `Grid` component. The layout is updated when a new
card is added to the grid.

Try clicking the "Save layout" button to save the current layout of the grid.
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
    for x in range(10)
]

app.layout = dmc.MantineProvider(
    [
        dmc.Stack(
            [
                dmc.Title(TITLE, order=2),
                dcc.Markdown(DESCRIPTION),
                dcc.Store(id="layout-store", data=initial_layout, storage_type="local"),
                dmc.Group(
                    [
                        dmc.Button(
                            "Save Layout",
                            id="save-layout",
                            size="lg",
                            variant="outline",
                        ),
                        dmc.Button(
                            "Load layout",
                            id="load-layout",
                            size="lg",
                            variant="outline",
                        ),
                        dmc.Button(
                            "Reset layout",
                            id="reset-layout",
                            size="lg",
                            variant="outline",
                        ),
                    ]
                ),
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
    Output("grid", "layout", allow_duplicate=True),
    Output("layout-store", "data"),
    Input("save-layout", "n_clicks"),
    Input("load-layout", "n_clicks"),
    Input("reset-layout", "n_clicks"),
    State("grid", "layout"),
    prevent_initial_call=True,
)
def save_layout(save_clicks, load_clicks, reset_clicks, layout):
    if ctx.triggered_id == "save-layout":
        return no_update, layout
    elif ctx.triggered_id == "reset-layout":
        return initial_layout, initial_layout
    return no_update, no_update


@app.callback(
    Output("grid", "layout"),
    Input("load-layout", "n_clicks"),
    State("layout-store", "data"),
)
def load_layout(n_clicks, layout):
    return layout


if __name__ == "__main__":
    app.run(debug=True)