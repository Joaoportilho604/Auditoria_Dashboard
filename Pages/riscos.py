import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/riscos",
    name="Riscos e Recomendações"
)

# ==================================================
# DADOS
# ==================================================

riscos = [

    {
        "risco": "Concentração excessiva da despesa em Vida Corrente",
        "probabilidade": "Alta",
        "impacto": "Alto",
        "nivel": "Elevado"
    },

    {
        "risco": "Subfinanciamento da Investigação",
        "probabilidade": "Alta",
        "impacto": "Médio",
        "nivel": "Elevado"
    },

    {
        "risco": "Ausência de monitorização sistemática de KPI",
        "probabilidade": "Média",
        "impacto": "Alto",
        "nivel": "Elevado"
    },

    {
        "risco": "Crescimento da despesa sem aumento proporcional dos resultados",
        "probabilidade": "Média",
        "impacto": "Alto",
        "nivel": "Elevado"
    },

    {
        "risco": "Estagnação da satisfação da Vida Corrente",
        "probabilidade": "Média",
        "impacto": "Médio",
        "nivel": "Moderado"
    }

]

# ==================================================
# LAYOUT
# ==================================================

layout = dbc.Container([

    html.H2(
        "Riscos e Recomendações",
        className="mb-4"
    ),
dbc.Row([

    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.H5("Riscos Elevados"),
                html.H2("4")
            ])
        )
    ),

    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.H5("Riscos Moderados"),
                html.H2("1")
            ])
        )
    ),

    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.H5("Recomendações"),
                html.H2("5")
            ])
        )
    )

], className="mb-4"),
    html.H4("Matriz de Risco"),

    dbc.Table(

        [

            html.Thead(

                html.Tr([

                    html.Th("Risco"),
                    html.Th("Probabilidade"),
                    html.Th("Impacto"),
                    html.Th("Nível")

                ])

            ),

            html.Tbody([

                html.Tr([

                    html.Td(r["risco"]),
                    html.Td(r["probabilidade"]),
                    html.Td(r["impacto"]),
                    html.Td(r["nivel"])

                ])

                for r in riscos

            ])

        ],

        bordered=True,
        striped=True,
        hover=True

    ),

    html.Br(),

    html.H4("Principais Achados"),

    html.Ul([

        html.Li(
            "87% do orçamento encontra-se concentrado na rubrica Vida Corrente."
        ),

        html.Li(
            "A Investigação continua a representar uma parcela reduzida do orçamento."
        ),

        html.Li(
            "Existe margem para reforçar a monitorização dos KPI de desempenho."
        ),

        html.Li(
            "O crescimento da despesa deve continuar a ser acompanhado pela evolução dos resultados."
        )

    ]),

    html.Br(),

    html.H4("Recomendações"),

    html.Ul([

        html.Li(
            "Implementar um sistema permanente de monitorização dos KPI."
        ),

        html.Li(
            "Reavaliar a estrutura da despesa de Vida Corrente."
        ),

        html.Li(
            "Reforçar progressivamente o investimento em Investigação."
        ),

        html.Li(
            "Associar a afetação de recursos aos resultados obtidos."
        ),

        html.Li(
            "Monitorizar regularmente os níveis de satisfação."
        )

    ]),

    html.Br(),

    dbc.Alert(

        "Conclusão: a organização apresenta desempenho global positivo, mas existem oportunidades para melhorar a distribuição dos recursos e reforçar os mecanismos de monitorização.",

        color="success"

    )

], fluid=True)
