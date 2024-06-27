from dash_grid_layout import Grid, GridItem
from dash import Dash, callback, html, Input, Output

app = Dash(__name__)

app.layout = html.Div(
    [
        Grid(
            id="input",
            children=[
                GridItem(
                    html.Div("This is a div"), id="b", x=1, y=0, width=2, height=1
                ),
                GridItem(
                    html.A("hello", href="#"), id="k", x=0, y=1, width=1, height=1
                ),
            ],
        ),
        html.Button("Add", id="add"),
    ]
)


@app.callback(
    Output("input", "children"),
    Input("add", "n_clicks"),
    Input("input", "children"),
    prevent_initial_call=True,
)
def add(n_clicks, children):
    return children + [
        GridItem(
            html.Div(f"This is div - {len(children)}"),
            id=f"item-{len(children)}",
            x=0,
            y=0,
            width=1,
            height=1,
        )
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
