import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State

from components.search_bar import search_bar
from components.bar_chart import bar_chart

external_stylesheets = [dbc.themes.DARKLY]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = "My App"

server = app.server

app.layout = html.Div(children=[
    html.H1("Hello World! And other beings!"),
    search_bar,
    html.Div(id="search-bar-output", children=[]),
    bar_chart
]
)


@app.callback(Output(component_id="search-bar-output", component_property="children"),
              [Input(component_id="search-bar-submit-button", component_property="n_clicks")],
              [State(component_id="search-bar", component_property="value")])
def render_output(n_clicks, text):
    if n_clicks == 0:
        return None
    print(text)
    if text is None or text == "":
        text = "You haven't entered anything"
    paragraph = f"{text} - {n_clicks} clicks"
    paragraph_component = html.P(paragraph.upper())
    return paragraph_component


# this checks 'was this file run directly?'
if __name__ == "__main__":
    app.run_server(host='localhost', debug=False)
