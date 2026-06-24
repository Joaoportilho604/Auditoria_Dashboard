from dash import Dash
from dash import html
from dash import dcc
from dash import page_container

import dash_bootstrap_components as dbc

from components.navbar import sidebar

app = Dash(

    __name__,

    use_pages=True,

    external_stylesheets=[
        dbc.themes.BOOTSTRAP
    ]

)

app.layout = html.Div([

    dcc.Location(id="url"),

    sidebar,

    html.Div([

        page_container,

        html.Hr(),

        html.Center([

            html.P(
                "Dashboard de Auditoria de Desempenho"
            ),

            html.P(
                "João Araújo | André Fernandes | João Lopes"
            ),

            html.P(
                "Ano Letivo 2025/2026"
            )

        ])

    ],

    className="content")

])

if __name__ == "__main__":
    app.run(debug=True)