"""
Gráficos de distribuição: histogramas(distribuição), boxplots, densidade, violin
Para análise de distribuições e outliers
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats


# Gráfico de Distribuição - histograma
def grafico_distribuicao(df: pd.DataFrame, column: str, kde=True, bins=30, color='purple'):
    """
    Plota a distribuição de uma coluna numérica.
    
    Parâmetros:
    df: dataframe
    column: coluna do dataframe
    kde: Kernel Density Estimation(Estimativa de Densidade por Kernel) - mostra uma curva suave que
    bins: intervalos que os dados serão divididos no histograma

    Retorna:
    Gráfico de distribuição (histplot)
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=kde, bins=bins, color=color)
    plt.title(f'Distribuição de {column}')
    plt.xlabel(column)
    plt.ylabel('Frequência')
    plt.show()


# Grráfico Boxplot
def grafico_boxplot(df: pd.DataFrame, column: str):
    """Plota um boxplot para uma coluna numérica."""
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[column])
    plt.title(f'Boxplot de {column}')
    plt.show()


def grafico_violin(df: pd.DataFrame, x=None, y=None, titulo='', 
                    figsize=(10, 6)):
    """
    Violin plot para ver distribuição detalhada
    """
    plt.figure(figsize=figsize)
    
    sns.violinplot(data=df, x=x, y=y)
    
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def grafico_densidade(df: pd.DataFrame, coluna, titulo='', xlabel='', 
                        figsize=(10, 6), comparar_normal=True):
    """
    Gráfico de densidade com comparação à distribuição normal
    
    Args:
        comparar_normal: sobrepor curva normal teórica
    """
    plt.figure(figsize=figsize)
    
    # Densidade dos dados
    df[coluna].plot(kind='density', color='blue', linewidth=2, label='Dados')
    
    # Comparar com normal se solicitado
    if comparar_normal:
        mean_val = df[coluna].mean()
        std_val = df[coluna].std()
        
        x = np.linspace(df[coluna].min(), df[coluna].max(), 100)
        normal_curve = stats.norm.pdf(x, mean_val, std_val)
        
        plt.plot(x, normal_curve, 'r--', linewidth=2, label='Normal teórica')
        plt.legend()
    
    plt.title(titulo or f'Densidade de {coluna}', fontsize=14, fontweight='bold')
    plt.xlabel(xlabel or coluna, fontsize=12)
    plt.ylabel('Densidade', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def grafico_qq(df: pd.DataFrame, coluna, titulo='', figsize=(8, 6)):
    """
    Q-Q plot para testar normalidade
    """
    plt.figure(figsize=figsize)
    
    stats.probplot(df[coluna].dropna(), dist="norm", plot=plt)
    
    plt.title(titulo or f'Q-Q Plot: {coluna}', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# Boxplot multiplos

def grafico_dist_boxplot(df: pd.DataFrame, colunas: list = None, bins: int = 30):
    '''
        Gráfico de distribuição e BoxPlot

        Parametro:
        df: Dataset
        colunas: lista com os nomes das colunas

        Return:
        Retorna os gráficos histograma e boxplot
    '''
    if colunas == None:
        colunas = df.columns

    for coluna in colunas:
        print(f'\n📊 Análise da coluna: {coluna}')

        # Plot da distribuição
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        sns.histplot(df[coluna], kde=True, bins=bins, color='purple')
        plt.title(f'Distribuição - {coluna}')

        plt.subplot(1, 2, 2)
        sns.boxplot(x=df[coluna], color='blue')
        plt.title(f'Boxplot - {coluna}')

        plt.tight_layout()
        plt.show()

# Boxplot bloco
def grafico_bloco_boxplot(df: pd.DataFrame, colunas: list):
    '''
    Gráficos de BoxPlot encadeados

    Parametro:
    df: Dataset
    colunas: lista com os nomes das colunas

    Return:
    Retorna os gráficos histograma e boxplot
    '''
    # Box Plots
    #colunas = []

    plt.figure(figsize=(12, 14))  # aumenta o tamanho para não ficar apertado

    for i, coluna in enumerate(colunas, 1):
        plt.subplot(len(colunas), 2, i)
        sns.boxplot(x=df[coluna], color='purple')
        plt.title(f'Boxplot - {coluna}')
        plt.xlabel('')
        plt.tight_layout()
        plt.show()