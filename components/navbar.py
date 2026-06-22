from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.H2("Auditoria", className="display-6"),
        html.Hr(),

        dbc.Nav(
            [
                dbc.NavLink(
                    "Resumo Executivo",
                    href="/",
                    active="exact"
                ),

                dbc.NavLink(
                    "Financeiro",
                    href="/financeiro",
                    active="exact"
                ),

                dbc.NavLink(
                    "Recursos Humanos",
                    href="/recursos",
                    active="exact"
                ),

                dbc.NavLink(
                    "Desempenho",
                    href="/desempenho",
                    active="exact"
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)
