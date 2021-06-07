import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


def get_options_from_dict(dict_):
    list_label_value = []
    for key_value, label in dict_.items():
        d = {"value": key_value, "label": label}
        list_label_value.append(d)
    return list_label_value


def get_item_radio_items(id, items, legend, value_idx=0):
    return dbc.FormGroup(
        [
            html.P(legend),
            dcc.RadioItems(
                id=id,
                options=get_options_from_dict(items),
                value=list(items.keys())[value_idx],
                labelStyle={"display": "inline-block", "margin": "5px"},
            ),
            html.Br(),
        ]
    )
