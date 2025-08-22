# etl/__init__.py
"""
Pacote ETL - Extract, Transform, Load
Módulos para processamento de dados
"""

# Importar funções principais do módulo transform
from .transform import (
    # Limpeza de dados
    remove_nulls,
    remove_duplicates,
    
    # Manipulação de colunas  
    clean_columns,
    rename_columns,
    
    # Tipos de dados
    padroniza_tipos_dados,
    
    # Função principal
    clean_dataframe
)

__version__ = "1.0.0"
__author__ = "Seu Nome"

# Definir o que será importado com 'from etl import *'
__all__ = [
    'remove_nulls',
    'remove_duplicates', 
    'clean_columns',
    'rename_columns',
    'padroniza_tipos_dados',
    'clean_dataframe'
]