import dash
from dash import html,dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

from components.dados import carregar_dados

dash.register_page(
    __name__,
    path="/recursos"
)

df = carregar_dados()

rh = pd.DataFrame({

    "Categoria":[
        "Oficiais",
        "Alunos",
        "Sargentos",
        "Praças",
        "Civis"
    ],

    "2023":[

        df["Of_2023"].sum(),
        df["Alun_2023"].sum(),
        df["Sarg_2023"].sum(),
        df["Pr_2023"].sum(),
        df["Civis_2023"].sum()
    ]
})

fig = px.bar(

    rh,

    x="Categoria",
    y="2023",

    title="Recursos Humanos Utilizados"
)

layout = dbc.Container([

    html.H2("Recursos Humanos"),

    dcc.Graph(
        figure=fig
    )

],fluid=True)