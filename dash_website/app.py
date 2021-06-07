import dash
import dash_bootstrap_components as dbc

APP = dash.Dash(
    name=__name__,
    external_stylesheets=[dbc.themes.CYBORG],
    title="Tutorial website",
)
APP.config.suppress_callback_exceptions = True
