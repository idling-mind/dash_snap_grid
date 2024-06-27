from dash_grid_layout import Grid
from dash import Dash, callback, html, Input, Output

app = Dash(__name__)

initial_layout = [
    {"i": "a", "x": 0, "y": 0, "w": 3, "h": 3},
    {"i": "b", "x": 1, "y": 0, "w": 1, "h": 1},
]

app.layout = html.Div(
    [
        Grid(
            id="input",
            layout=initial_layout,
            children=[
                html.Div(id="a", children="This is div - 0"),
                html.Div(id="b", children="This is div - 1"),
            ],
        ),
        html.Button("Update Layout", id="reset-layout"),
    ]
)

@app.callback(Output("a", "children"), Input("input", "layout"))
def update_layout(layout):
    return str(layout)

@app.callback(Output("input", "layout"), Input("reset-layout", "n_clicks"))
def reset_layout(n_clicks):
    return initial_layout


if __name__ == '__main__':
    app.run_server(debug=True)
