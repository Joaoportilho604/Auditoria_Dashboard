import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from components.dados import carregar_dados

dash.register_page(
    __name__,
    path="/recursos",
    name="Recursos Humanos"
)

# ==================================================
# DADOS
# ==================================================

df = carregar_dados()

rh = pd.DataFrame({

    "Categoria":[
        "Oficiais",
        "Alunos",
        "Sargentos",
        "Praças",
        "Civis"
    ],

    "2022":[
        df["Of_2022"].sum(),
        df["Alun_2022"].sum(),
        df["Sarg_2022"].sum(),
        df["Pr_2022"].sum(),
        df["Civis_2022"].sum()
    ],

    "2023":[
        df["Of_2023"].sum(),
        df["Alun_2023"].sum(),
        df["Sarg_2023"].sum(),
        df["Pr_2023"].sum(),
        df["Civis_2023"].sum()
    ]

})

# ==================================================
# GRÁFICO
# ==================================================

rh_long = rh.melt(
    id_vars="Categoria",
    var_name="Ano",
    value_name="Quantidade"
)

fig = px.bar(
    rh_long,
    x="Categoria",
    y="Quantidade",
    color="Ano",
    barmode="group",
    title="Comparação Recursos Humanos 2022 vs 2023"
)

# ==================================================
# LAYOUT
# ==================================================

layout = dbc.Container([

    html.H2(
        "Recursos Humanos",
        className="mb-4"
    ),

    dcc.Graph(
        figure=fig
    ),

    html.Hr(),

    html.H3("Principais Conclusões"),

    html.Ul([

        html.Li(
            "O número total de alunos aumentou entre 2022 e 2023."
        ),

        html.Li(
            "A procura pela formação registou crescimento significativo."
        ),

        html.Li(
            "Verifica-se crescimento dos recursos afetos à atividade."
        ),

        html.Li(
            "Os indicadores sugerem maior capacidade operacional em 2023."
        )

    ])

], fluid=True)
