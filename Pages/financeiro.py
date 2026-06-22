import dash
from dash import html,dcc
import dash_bootstrap_components as dbc

import plotly.express as px

from components.dados import carregar_dados

dash.register_page(
    __name__,
    path="/financeiro"
)

df = carregar_dados()

top_despesas = (
    df.groupby("Despesa_Legal")["Dotacao_2023"]
    .sum()
    .reset_index()
    .sort_values(
        "Dotacao_2023",
        ascending=False
    )
    .head(10)
)

fig_top = px.bar(
    top_despesas,
    x="Dotacao_2023",
    y="Despesa_Legal",
    orientation="h",
    title="Top 10 Despesas"
)

objetivos = (
    df.groupby("Objetivo")["Dotacao_2023"]
    .sum()
    .reset_index()
)

fig_obj = px.bar(
    objetivos.head(10),
    x="Objetivo",
    y="Dotacao_2023",
    title="Top 10 Objetivos"
)

fig_obj.update_layout(
    height=500
)
layout = dbc.Container([

    html.H2("Análise Financeira"),

    dcc.Graph(figure=fig_top),

    dcc.Graph(figure=fig_obj)

],fluid=True)   