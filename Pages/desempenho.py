import dash
from dash import html,dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

dash.register_page(
    __name__,
    path="/desempenho"
)

satisf = pd.DataFrame({

    "Área":[
        "Formação",
        "Investigação",
        "Ensino",
        "Vida Corrente"
    ],

    "Satisfação":[
        4.1,
        4.1,
        4.4,
        3.8
    ]
})

fig = px.bar(

    satisf,

    x="Área",
    y="Satisfação",

    title="Grau de Satisfação"
)

layout = dbc.Container([

    html.H2("Desempenho"),

    dbc.Row([

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Custo por Aluno"),
                    html.H2("11 758 €")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Eficiência"),
                    html.H2("▲ 11 %")
                ])
            )
        ),

    ],className="mb-4"),

    dcc.Graph(
        figure=fig
    )

],fluid=True)