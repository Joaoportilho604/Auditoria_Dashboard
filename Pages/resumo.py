import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

dash.register_page(
    __name__,
    path="/",
    name="Resumo Executivo"
)

# =========================
# DADOS
# =========================

orcamento_2022 = 1429069
orcamento_2023 = 1646150

alunos_2022 = 110
alunos_2023 = 140

crescimento = round(
    ((orcamento_2023 - orcamento_2022)
    / orcamento_2022) * 100,
    1
)

satisfacao_media = 4.1

# =========================
# GRAFICO EVOLUCAO
# =========================

df_orc = pd.DataFrame({

    "Ano":[2022,2023],
    "Orçamento":[orcamento_2022,orcamento_2023]

})

fig_orc = px.bar(
    df_orc,
    x="Ano",
    y="Orçamento",
    text_auto=True,
    title="Evolução do Orçamento"
)

# =========================
# DISTRIBUICAO
# =========================

df_area = pd.DataFrame({

    "Área":[
        "Formação",
        "Investigação",
        "Ensino",
        "Vida Corrente"
    ],

    "Valor":[
        133700,
        12044,
        66850,
        1433557
    ]
})

fig_area = px.pie(
    df_area,
    names="Área",
    values="Valor",
    hole=0.5,
    title="Distribuição Orçamental 2023"
)

layout = dbc.Container([

    html.H2(
        "Resumo Executivo",
        className="mb-4"
    ),

    dbc.Row([

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("Orçamento 2022"),
                    html.H3(f"{orcamento_2022:,.0f} €")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("Orçamento 2023"),
                    html.H3(f"{orcamento_2023:,.0f} €")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("Crescimento"),
                    html.H3(f"{crescimento}%")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("Satisfação"),
                    html.H3(str(satisfacao_media))
                ])
            )
        ),

    ], className="mb-4"),

    dbc.Row([

        dbc.Col(
            dcc.Graph(
                figure=fig_orc
            ),
            width=6
        ),

        dbc.Col(
            dcc.Graph(
                figure=fig_area
            ),
            width=6
        )

    ])

], fluid=True)