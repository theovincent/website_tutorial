from dash_website.app import APP
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import numpy as np

from dash_website.utils.aws_loader import load_feather
from dash_website.utils.controls import get_item_radio_items
from dash_website.scores import SCORES


def get_controls_scores():
    return dbc.Card([get_item_radio_items("metric_scores", SCORES, "Select a metric: ")])


@APP.callback(
    [Output("graph_scores", "figure"), Output("title_scores", "children")],
    Input("metric_scores", "value"),
)
def _fill_graph_scores(metric):
    import plotly.graph_objs as go

    scores = load_feather("website_tutorial/scores.feather")

    scores["model"] = scores["dimension"].copy()
    for columns in ["subdimension", "sub_subdimension", "algorithm"]:
        scores["model"] += " / " + scores[columns]
    scores.set_index("model", inplace=True)

    selected_scores = scores.loc[scores.index[np.random.randint(0, high=scores.shape[0], size=10)]]

    bars = go.Bar(x=selected_scores.index, y=selected_scores[metric])

    fig = go.Figure(bars)

    fig.update_layout(
        yaxis={"title": SCORES[metric], "showgrid": False, "zeroline": False, "title_font": {"size": 25}},
        xaxis={"showgrid": False, "zeroline": False, "tickangle": 90},
        height=800,
        margin={"l": 0, "r": 0, "b": 0, "t": 0},
    )

    return fig, f"The average {SCORES[metric]} is {selected_scores[metric].mean().round(3)}"


LAYOUT = dbc.Container(
    [
        html.H1("Scores"),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        get_controls_scores(),
                        html.Br(),
                        html.Br(),
                    ],
                    width={"size": 3},
                ),
                dbc.Col(
                    [
                        dcc.Loading(
                            [
                                html.H2(id="title_scores"),
                                dcc.Graph(id="graph_scores"),
                            ]
                        )
                    ],
                    width={"size": 9},
                ),
            ]
        ),
    ],
    fluid=True,
)
