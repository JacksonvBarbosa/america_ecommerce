import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def one_hot_encode(df: pd.DataFrame, columns: list, drop_first: bool = True) -> pd.DataFrame:
    """
    Aplica One-Hot Encoding nas colunas especificadas.

    Parâmetros:
    ----------
    df : pd.DataFrame
        DataFrame de entrada.
    columns : list
        Lista de colunas categóricas para codificação.
    drop_first : bool
        Remove a primeira categoria para evitar multicolinearidade (padrão: True).

    Retorna:
    -------
    pd.DataFrame
        DataFrame com colunas codificadas.
    """
    encoder = OneHotEncoder(drop='first' if drop_first else None, sparse_output=False)
    encoded_array = encoder.fit_transform(df[columns])
    encoded_df = pd.DataFrame(
        encoded_array,
        columns=encoder.get_feature_names_out(columns),
        index=df.index
    )

    df_encoded = pd.concat([df.drop(columns, axis=1), encoded_df], axis=1)
    return df_encoded
