from dash_website.app import APP
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from dash_website.utils.aws_loader import load_npy
from dash_website.utils.controls import get_item_radio_items
from dash_website import SEX_LEGEND


@APP.callback(Output("graph_time_series", "figure"), Input("sex_time_series", "value"))
def _display_left_time_series(sex):
    import plotly.graph_objs as go

    time_series = load_npy(f"website_tutorial/{sex}.npy")

    scatter = go.Scatter(y=time_series, mode="markers", marker={"size": 5})

    fig = go.Figure(scatter)

    fig.update_layout(
        {
            "xaxis": {"title": "Time", "title_font": {"size": 25}},
            "yaxis": {"title": "Lungs volume", "title_font": {"size": 25}},
            "margin": {"l": 0, "r": 0, "b": 0, "t": 0},
        }
    )

    return fig


LAYOUT = dbc.Container(
    [
        html.H1("Time series"),
        html.Br(),
        html.Br(),
        dbc.Row([dbc.Col(dbc.Card([get_item_radio_items(f"sex_time_series", SEX_LEGEND, "Select sex :")]))]),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Loading(
                        [
                            html.H3("An example of a time series"),
                            dcc.Graph(id="graph_time_series"),
                        ]
                    )
                ),
            ]
        ),
    ],
    fluid=True,
)
