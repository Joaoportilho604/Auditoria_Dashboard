import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

dash.register_page(
    __name__,
    path="/financeiro",
    name="Financeiro"
)

# ==================================================
# DADOS
# ==================================================

orcamento_2022 = 1429069
orcamento_2023 = 1646150

crescimento = round(
    ((orcamento_2023 - orcamento_2022)
    / orcamento_2022) * 100,
    1
)

# ==================================================
# COMPARAÇÃO 2022 VS 2023
# ==================================================

df_comp = pd.DataFrame({

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

    "Valor":[
        113700,
        10444,
        60368,
        1244557,
        133700,
        12044,
        66850,
        1433557
    ]
})

fig_comp = px.bar(
    df_comp,
    x="Área",
    y="Valor",
    color="Ano",
    barmode="group",
    title="Comparação Financeira 2022 vs 2023"
)

# ==================================================
# DISTRIBUIÇÃO 2023
# ==================================================

df_pie = pd.DataFrame({

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

fig_pie = px.pie(
    df_pie,
    names="Área",
    values="Valor",
    hole=0.5,
    title="Distribuição Orçamental 2023"
)

# ==================================================
# TABELA DE COMPARAÇÃO
# ==================================================

df_tabela = pd.DataFrame({

    "Área":[
        "Formação",
        "Investigação",
        "Ensino",
        "Vida Corrente"
    ],

    "2022":[
        113700,
        10444,
        60368,
        1244557
    ],

    "2023":[
        133700,
        12044,
        66850,
        1433557
    ]
})

df_tabela["Diferença"] = (
    df_tabela["2023"] - df_tabela["2022"]
)

df_tabela["% Crescimento"] = round(
    (
        df_tabela["Diferença"]
        / df_tabela["2022"]
    ) * 100,
    1
)

# ==================================================
# LAYOUT
# ==================================================

layout = dbc.Container([

    html.H2(
        "Análise Financeira",
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

    ], className="mb-4"),

    dbc.Row([

        dbc.Col(
            dcc.Graph(
                figure=fig_pie
            ),
            width=5
        ),

        dbc.Col(
            dcc.Graph(
                figure=fig_comp
            ),
            width=7
        )

    ]),

    html.Hr(),

    html.H3("Tabela Comparativa"),

    dbc.Table.from_dataframe(
        df_tabela,
        striped=True,
        bordered=True,
        hover=True
    ),

    html.Br(),

    html.H4("Principais Conclusões"),

    html.Ul([

        html.Li(
            "O orçamento aumentou 15,2% entre 2022 e 2023."
        ),

        html.Li(
            "Vida Corrente continua a representar a maior parcela do orçamento."
        ),

        html.Li(
            "A área de Formação apresentou crescimento significativo."
        ),

        html.Li(
            "Todas as áreas registaram crescimento positivo."
        )

    ])

], fluid=True)