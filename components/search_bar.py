import dash_bootstrap_components as dbc
import dash_html_components as html

search_bar = html.Div(id="search-bar-container", children=
    [
        dbc.Input(id="search-bar", placeholder="Wubba Lubba Dub Dub", type="text"),
        dbc.Button("SHOW ME WHAT YOU GOT", id="search-bar-submit-button", color="primary", className="mr-1", n_clicks=0)
    ])
