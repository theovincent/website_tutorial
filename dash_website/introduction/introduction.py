import dash_bootstrap_components as dbc
import dash_html_components as html


LAYOUT = html.Div(
    [
        html.Div(
            [
                dbc.Row(
                    dbc.Col(
                        html.P("Website tutorial", style={"padding-top": "50px"}),
                        style={"width": 8, "text-align": "center", "fontSize": 70},
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        html.Div(
                            [
                                html.P(
                                    [
                                        "This website is a tutorial to show how Dash works. You can find the source code ",
                                        html.A("here", href="https://github.com/HMS-Internship/Website_tutorial"),
                                        ".",
                                    ]
                                ),
                            ],
                            style={"fontSize": 20, "padding": 15, "text-align": "justify", "text-indent": 30},
                        ),
                        width=11,
                    ),
                    justify="center",
                    style={"padding-top": "10px"},
                ),
            ],
            style={"padding-bottom": 100},
        ),
    ]
)
