import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

dash.register_page(
    __name__,
    path="/",
    name="Resumo Executivo"
)

# ==================================================
# DADOS
# ==================================================

orcamento_2022 = 1429069
orcamento_2023 = 1646150

alunos_2022 = 110
alunos_2023 = 140

satisfacao_media = 4.1

# ==================================================
# KPI'S
# ==================================================

crescimento_orcamento = round(
    ((orcamento_2023 - orcamento_2022)
     / orcamento_2022) * 100,
    1
)

crescimento_alunos = round(
    ((alunos_2023 - alunos_2022)
     / alunos_2022) * 100,
    1
)

custo_aluno_2022 = round(
    orcamento_2022 / alunos_2022
)

custo_aluno_2023 = round(
    orcamento_2023 / alunos_2023
)

eficiencia = round(
    ((custo_aluno_2022 - custo_aluno_2023)
     / custo_aluno_2022) * 100,
    1
)

concentracao = round(
    (1433557 / orcamento_2023) * 100,
    1
)

peso_investigacao = round(
    (12044 / orcamento_2023) * 100,
    2
)

# ==================================================
# GRAFICO ORÇAMENTO
# ==================================================

df_orc = pd.DataFrame({

    "Ano":[
        "2022",
        "2023"
    ],

    "Orçamento":[
        orcamento_2022,
        orcamento_2023
    ]

})

fig_orc = px.bar(
    df_orc,
    x="Ano",
    y="Orçamento",
    text_auto=True,
    title="Evolução do Orçamento"
)

# ==================================================
# GRAFICO DISTRIBUIÇÃO
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
# COMPARAÇÃO FINANCEIRA
# ==================================================

df_fin = pd.DataFrame({

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

fig_fin = px.bar(
    df_fin,
    x="Área",
    y="Valor",
    color="Ano",
    barmode="group",
    title="Comparação Financeira 2022 vs 2023"
)

# ==================================================
# LAYOUT
# ==================================================

layout = dbc.Container([

    html.H2(
        "Resumo Executivo",
        className="mb-2"
    ),

    html.H5(
        "Período de Auditoria: 2022 - 2023",
        className="text-muted mb-4"
    ),

    dbc.Row([

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("💰 Orçamento 2022"),
                    html.H3(f"{orcamento_2022:,.0f} €")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("💰 Orçamento 2023"),
                    html.H3(f"{orcamento_2023:,.0f} €")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("📈 Crescimento"),
                    html.H3(f"{crescimento_orcamento}%")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("⭐ Satisfação"),
                    html.H3(f"{satisfacao_media}")
                ])
            )
        )

    ], className="mb-4"),

    dbc.Row([

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("👨‍🎓 Crescimento Alunos"),
                    html.H3(f"{crescimento_alunos}%")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("💶 Custo por Aluno"),
                    html.H3(f"{custo_aluno_2023:,.0f} €")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("⚙️ Eficiência"),
                    html.H3(f"{eficiencia}%")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("🏆 Melhor Área"),
                    html.H3("Ensino")
                ])
            )
        ),

        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("🔬 Investigação"),
                    html.H3(f"{peso_investigacao}%")
                ])
            )
        )

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
                figure=fig_pie
            ),
            width=6
        )

    ]),

    dbc.Row([

        dbc.Col(
            dcc.Graph(
                figure=fig_fin
            ),
            width=12
        )

    ]),

    html.Hr(),

    html.H3("Principais Conclusões"),

    html.Ul([

        html.Li(
            "O orçamento aumentou 15,2% entre 2022 e 2023."
        ),

        html.Li(
            "O número de alunos cresceu 27,3%."
        ),

        html.Li(
            "O custo por aluno diminuiu."
        ),

        html.Li(
            "Ensino apresenta o melhor desempenho."
        ),

        html.Li(
            "87% do orçamento encontra-se concentrado em Vida Corrente."
        )

    ]),

    dbc.Alert(

        "Conclusão Global: A Academia Militar apresentou crescimento financeiro, aumento do número de alunos e melhoria da eficiência operacional entre 2022 e 2023.",

        color="success"

    )

], fluid=True)