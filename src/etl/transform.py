# etl/transform.py
"""
Módulo principal de transformação
Importa e organiza todas as funções de transformação
"""

# Importar todas as funções dos módulos específicos
from .data_cleaning import (
    remove_nulls,
    remove_duplicates
)

from .column_utils import (
    clean_columns,
    rename_columns
)

from .data_types import (
    padroniza_tipos_dados
)

# Libs necessárias para o módulo
import pandas as pd
import numpy as np
from typing import List, Dict, Optional


# Função principal que combina várias transformações
def clean_dataframe(df, 
                    null_strategy='drop', 
                    remove_dups=True,
                    clean_cols=True,
                    standardize_types=True,
                    verbose=True):
    """
    Aplica limpeza completa no DataFrame
    
    Args:
        df: DataFrame a ser limpo
        null_strategy: estratégia para nulos
        remove_dups: remover duplicatas
        clean_cols: limpar nomes das colunas
        standardize_types: padronizar tipos
        verbose: mostrar progresso
    
    Returns:
        DataFrame limpo
    """
    df_clean = df.copy()
    
    if verbose:
        print("🚀 INICIANDO LIMPEZA COMPLETA")
        print(f"📊 Dataset original: {df_clean.shape}")
    
    # 1. Limpar nomes das colunas
    if clean_cols:
        df_clean = clean_columns(df_clean, verbose=verbose)
    
    # 2. Remover nulos
    df_clean = remove_nulls(df_clean, strategy=null_strategy, verbose=verbose)
    
    # 3. Remover duplicatas
    if remove_dups:
        df_clean = remove_duplicates(df_clean, verbose=verbose)
    
    # 4. Padronizar tipos
    if standardize_types:
        df_clean = padroniza_tipos_dados(df_clean, auto_detect=True, verbose=verbose)
    
    if verbose:
        print(f"✅ LIMPEZA CONCLUÍDA: {df_clean.shape}")
    
    return df_clean


# Exportar todas as funções para facilitar importação
__all__ = [
    'remove_nulls',
    'remove_duplicates', 
    'clean_columns',
    'rename_columns',
    'padroniza_tipos_dados',
    'clean_dataframe'
]