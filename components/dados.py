import pandas as pd

excel_file = "dados/Base dados auditoria desempenho.xlsx"

def carregar_dados():

    df_mapa = pd.read_excel(
        excel_file,
        sheet_name="Mapa",
        header=None
    )

    headers = [
        "Objetivo","Tipo_Atividade","Atividade",
        "Acao","Elemento_Acao",
        "Cod_Economica","Despesa_Legal",
        "Dotacao_2022","Dotacao_2023",
        "Of_2022","Alun_2022","Sarg_2022",
        "Pr_2022","Civis_2022",
        "Of_2023","Alun_2023","Sarg_2023",
        "Pr_2023","Civis_2023"
    ]

    df = df_mapa.iloc[11:,3:22].copy()
    df.columns = headers

    df = df.dropna(subset=["Objetivo"])

    numericas = [
        "Dotacao_2022","Dotacao_2023",
        "Of_2022","Alun_2022","Sarg_2022",
        "Pr_2022","Civis_2022",
        "Of_2023","Alun_2023","Sarg_2023",
        "Pr_2023","Civis_2023"
    ]

    for c in numericas:
        df[c] = pd.to_numeric(
            df[c],
            errors="coerce"
        ).fillna(0)

    return df