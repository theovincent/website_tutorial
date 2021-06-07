import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from dash_website.app import APP

import dash_website.introduction.introduction as introduction
import dash_website.time_series.time_series as time_series
import dash_website.scores.scores as scores


def get_server():
    add_layout(APP)
    return APP.server


def launch_local_website():
    add_layout(APP)
    APP.run_server(debug=True, port=8080)


def add_layout(app):
    app.layout = html.Div(
        [dcc.Location(id="url", refresh=False), get_top_bar(), html.Hr(), html.Div(id="page_content")],
        style={"height": "100vh", "fontSize": 14},
    )


def get_top_bar():
    return html.Div(
        [
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("Introduction", href="/", active=True, id="introduction")),
                    dbc.NavItem(dbc.NavLink("Time series", href="/time_series", id="time_series")),
                    dbc.NavItem(dbc.NavLink("Scores", href="/scores", id="scores")),
                ],
                fill=True,
                pills=True,
            ),
        ],
        style={"top": 0, "left": 50, "bottom": 0, "right": 50, "padding": "1rem 1rem"},
    )


@APP.callback(Output("page_content", "children"), Input("url", "pathname"))
def _display_page(pathname):
    if "time_series" == pathname.split("/")[1]:
        layout = time_series.LAYOUT

    elif "scores" == pathname.split("/")[1]:
        layout = scores.LAYOUT

    elif "/" == pathname:
        layout = introduction.LAYOUT

    else:
        layout = "404"

    return layout


@APP.callback(
    [Output("introduction", "active"), Output("time_series", "active"), Output("scores", "active")],
    Input("url", "pathname"),
)
def _change_active_page(pathname):
    active_pages = [False] * 3

    if "time_series" == pathname.split("/")[1]:
        active_pages[1] = True
    elif "scores" == pathname.split("/")[1]:
        active_pages[2] = True
    elif "/" == pathname:
        active_pages[0] = True

    return active_pages
