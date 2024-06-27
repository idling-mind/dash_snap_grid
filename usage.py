from dash_grid_layout import ResponsiveGrid
from dash import Dash, callback, html, Input, Output

app = Dash(__name__)

initial_layout = [
    {"i": "a", "x": 0, "y": 0, "w": 2, "h": 1},
    {"i": "b", "x": 1, "y": 0, "w": 1, "h": 1},
]

app.layout = [
    html.Div(
        [
            ResponsiveGrid(
                id="input",
                layouts={"lg": initial_layout},
                children=[
                    html.Div(id="a", children="This is div - 0"),
                    html.Div(id="b", children="This is div - 1"),
                ],
            ),
        ]
    ),
    html.Button("Update Layout", id="update-layout"),
]


@app.callback(Output("a", "children"), Input("input", "layouts"))
def update_layout(layout):
    return str(layout)


if __name__ == '__main__':
    app.run_server(debug=True)
