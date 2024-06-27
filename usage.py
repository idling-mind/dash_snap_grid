from dash_grid_layout import Grid
from dash import Dash, callback, html, Input, Output

app = Dash(__name__)

app.layout = html.Div(
    [
        Grid(
            id="input",
            layout=[
                {"i": "a", "x": 0, "y": 0, "w": 3, "h": 3, "static": True},
                {"i": "b", "x": 1, "y": 0, "w": 1, "h": 1},
            ],
            children=[
                html.Div(id="a", children="This is div - 0"),
                html.Div(id="b", children="This is div - 1"),
            ],
        ),
    ]
)

@app.callback(Output("a", "children"), Input("input", "layout"))
def update_layout(layout):
    return str(layout)


if __name__ == '__main__':
    app.run_server(debug=True)
