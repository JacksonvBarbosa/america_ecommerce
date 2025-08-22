import pandas as pd
from src.features.encoding import one_hot_encode

def prepare_data_for_model(df: pd.DataFrame, columns: list = None) -> pd.DataFrame:
    """
    Prepara os dados para treinar modelos de Machine Learning.
    
    Parâmetros:
    ----------
    df : pd.DataFrame
        DataFrame original.
    columns : list, opcional
        Lista de colunas específicas para aplicar One-Hot Encoding.
        Se None, aplica em todas as colunas categóricas.
    """
    # 1. Definir colunas categóricas
    if columns is None:
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    else:
        categorical_cols = columns

    # 2. Aplicar One-Hot Encoding
    df = one_hot_encode(df, categorical_cols, drop_first=True)

    # 3. (Opcional) Normalização, imputação, etc.
    # df = normalize_features(df)

    return df

