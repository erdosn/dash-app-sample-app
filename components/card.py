import dash_bootstrap_components as dbc
import dash_html_components as html


card = dbc.Card(
    [
        dbc.CardImg(src="https://ih1.redbubble.net/image.1125271744.4732/fposter,small,wall_texture,product,750x1000.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)