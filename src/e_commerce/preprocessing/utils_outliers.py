import pandas as pd
import numpy as np


def detect_outliers_iqr(df: pd.DataFrame, columns: list, factor: float = 1.5):
    """
    Detecta outliers em colunas numéricas usando o método IQR (Interquartile Range).
    Retorna um DataFrame com os índices dos outliers.
    """
    outliers = {}
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower, upper = Q1 - factor * IQR, Q3 + factor * IQR
        outliers[col] = df[(df[col] < lower) | (df[col] > upper)].index.tolist()
    return outliers


def remove_outliers(df: pd.DataFrame, columns: list, factor: float = 1.5):
    """
    Remove outliers das colunas especificadas.
    """
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower, upper = Q1 - factor * IQR, Q3 + factor * IQR
        df = df[(df[col] >= lower) & (df[col] <= upper)]
    return df.reset_index(drop=True)


def summarize_dataframe(df: pd.DataFrame):
    """
    Retorna um resumo básico do DataFrame:
    - tipos
    - valores nulos
    - valores únicos
    - amostra de dados
    """
    summary = pd.DataFrame({
        "Tipo": df.dtypes,
        "Nulos (%)": df.isnull().mean() * 100,
        "Valores únicos": df.nunique()
    })
    print("\nResumo do DataFrame:\n")
    print(summary)
    print("\nAmostra dos dados:\n")
    print(df.head())

'''
🛠️ Modifique quando for iniciar um projeto:

Ajuste a função remove_outliers se quiser outro método (Z-score, IsolationForest etc.).

Pode adicionar funções específicas, como normalização de colunas personalizadas.
'''