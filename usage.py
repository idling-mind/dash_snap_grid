import dash
from dash import html
from dash_snap_grid import ResponsiveGrid as Grid

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        Grid(
            id="grid",
            cols={"lg": 5, "md": 4, "sm": 3, "xs": 2, "xxs": 1},
            rowHeight=100,
            persistLayout=True,
            layouts={"lg":[
                # i should match the id of the children
                {"i": "1", "x": 0, "y": 0, "w": 1, "h": 2},
                {"i": "2", "x": 1, "y": 0, "w": 3, "h": 2},
                {"i": "3", "x": 4, "y": 0, "w": 1, "h": 2},
            ]},
            children=[
                html.Div(
                    "1", id="1", style={"background": "lightblue", "height": "100%"}
                ),
                html.Div(
                    "2", id="2", style={"background": "lightgreen", "height": "100%"}
                ),
                html.Div(
                    "3", id="3", style={"background": "lightcoral", "height": "100%"}
                ),
            ],
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
