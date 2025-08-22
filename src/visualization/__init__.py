# visualization/__init__.py
"""
Pacote de Visualização de Dados
Módulos organizados por tipo de gráfico e análise
"""

# Importar gráficos básicos
from .basic_charts import (
    grafico_barra,
    grafico_linha,
    grafico_pizza,
    grafico_area
)

# Importar gráficos de distribuição
from .distribution_charts import (
    grafico_histograma,
    grafico_boxplot,
    grafico_violin,
    grafico_densidade,
    grafico_qq
)

# Importar gráficos de relacionamento
from .relationship_charts import (
    grafico_dispersao,
    grafico_dispersao_categorico,
    matriz_correlacao,
    grafico_pairplot,
    grafico_regressao_multipla
)

# Importar gráficos avançados
from .advanced_charts import (
    dashboard_basico,
    grafico_serie_temporal,
    grafico_multiplos_subplots,
    grafico_antes_depois,
    heatmap_temporal
)

__version__ = "1.0.0"
__author__ = "Seu Nome"

# Definir o que será importado com 'from visualization import *'
__all__ = [
    # Básicos
    'grafico_barra',
    'grafico_linha', 
    'grafico_pizza',
    'grafico_area',
    
    # Distribuição
    'grafico_histograma',
    'grafico_boxplot',
    'grafico_violin',
    'grafico_densidade',
    'grafico_qq',
    
    # Relacionamento
    'grafico_dispersao',
    'grafico_dispersao_categorico',
    'matriz_correlacao',
    'grafico_pairplot',
    'grafico_regressao_multipla',
    
    # Avançados
    'dashboard_basico',
    'grafico_serie_temporal',
    'grafico_multiplos_subplots',
    'grafico_antes_depois',
    'heatmap_temporal'
]