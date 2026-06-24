import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

dash.register_page(
    __name__,
    path="/desempenho",
    name="Desempenho"
)

# ==================================================
# SATISFAÇÃO 2022 VS 2023
# ==================================================

satisf = pd.DataFrame({

    "Área":[
        "Formação",
        "Investigação",
        "Ensino",
        "Vida Corrente",
        "Formação",
        "Investigação",
        "Ensino",
        "Vida Corrente"
    ],

    "Ano":[
        "2022",
        "2022",
        "2022",
        "2022",
        "2023",
        "2023",
        "2023",
        "2023"
    ],

    "Satisfação":[
        4.1,
        3.8,
        4.1,
        3.8,
        4.1,
        4.1,
        4.4,
        3.8
    ]

})

fig_satisf = px.bar(
    satisf,
    x="Área",
    y="Satisfação",
    color="Ano",
    barmode="group",
    title="Comparação da Satisfação 2022 vs 2023"
)

# ==================================================
# EVOLUÇÃO DA SATISFAÇÃO
# ==================================================

df_evolucao = pd.DataFrame({

    "Área":[
        "Formação",
        "Investigação",
        "Ensino",
        "Vida Corrente"
    ],

    "Variação (%)":[
        0,
        7.9,
        7.3,
        0
    ]

})

fig_evolucao = px.bar(
    df_evolucao,
    x="Área",
    y="Variação (%)",
    title="Variação Percentual da Satisfação"
)

# ==================================================
# KPI'S
# ==================================================

custo_aluno = 955
produtividade = 0.001047

# ==================================================
# LAYOUT
# ==================================================

layout = dbc.Container([

    html.H2(
        "Desempenho e Eficácia",
        className="mb-4"
    ),

    dbc.Row([

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("Custo por Aluno"),
                    html.H3(f"{custo_aluno} €")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("Produtividade"),
                    html.H3(f"{produtividade}")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("Formação"),
                    html.H3("4.1")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("Ensino"),
                    html.H3("4.4")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("Investigação"),
                    html.H3("4.1")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("Vida Corrente"),
                    html.H3("3.8")
                ])
            )
        )

    ], className="mb-4"),

    dbc.Row([

        dbc.Col(
            dcc.Graph(
                figure=fig_satisf
            ),
            width=12
        )

    ]),

    dbc.Row([

        dbc.Col(
            dcc.Graph(
                figure=fig_evolucao
            ),
            width=12
        )

    ]),

    html.Hr(),

    html.H3("Conclusões da Auditoria"),

    html.Ul([

        html.Li(
            "O número de alunos cresceu 27,3% entre 2022 e 2023."
        ),

        html.Li(
            "O custo por aluno diminuiu de 1.034 € para 955 €."
        ),

        html.Li(
            "A produtividade da formação aumentou."
        ),

        html.Li(
            "Ensino apresenta o maior nível de satisfação."
        ),

        html.Li(
            "Investigação apresentou a maior evolução percentual."
        )

    ])

], fluid=True)