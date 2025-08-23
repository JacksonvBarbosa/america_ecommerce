"""
Gráficos de relacionamento: dispersão, correlação, heatmaps
Para análise de relações entre variáveis
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Gráfico de Dispersão (Scatterplot)
def grafico_dispersao(df: pd.DataFrame, x, y, color='blue', alpha=0.7, 
                        titulo='', ylabel='', xlabel='', figsize=(10, 6),
                        linha_regressao=True, cor_regressao='red'):
    """
    Gráfico de dispersão com linha de regressão opcional
    
    Args:
        df: dataframe
        x: coluna do df no eixo x (horizontal)
        y: coluna do df no eixo y (vertical)
        color: cor dos pontos no gráfico
        alpha: transpârencia dos pontos no gráfico 
        titulo: titulo do gráfico
        xlabel: rótulo do eixo x
        ylabel: rótulo do eixo y
        linha_regressao: mostrar linha de regressão
        cor_regressao: cor da linha de regressão

    """
    plt.figure(figsize=figsize)

    # Scatter plot
    sns.scatterplot(data=df, x=x, y=y, color=color, alpha=alpha)
    
    # Linha de regressão
    if linha_regressao:
        sns.regplot(data=df, x=x, y=y, 
                    scatter=False, line_kws={'color': cor_regressao, 'linewidth': 2})
    
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel or x, fontsize=12)
    plt.ylabel(ylabel or y, fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()


def grafico_dispersao_categorico(df: pd.DataFrame, x, y, categoria, 
                                titulo='', figsize=(10, 6), alpha=0.7):
    """
    Scatter plot colorido por categoria
    
    Args:
        df: dataframe
        x: coluna do df no eixo x (horizontal)
        y: coluna do df no eixo y (vertical)
        categoria: coluna categórica para colorir pontos
        titulo: titulo do gráfico
    """
    plt.figure(figsize=figsize)
    
    sns.scatterplot(data=df, x=x, y=y, hue=categoria, alpha=alpha)
    
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.xlabel(x, fontsize=12)
    plt.ylabel(y, fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()


def grafico_matriz_correlacao(df: pd.DataFrame, colunas=None, metodo='pearson',
                        titulo='Matriz de Correlação', figsize=(10, 8),
                        cmap='coolwarm', fmt='.2f', mostrar_valores=True):
    """
    Heatmap de correlação
    
    Args:
        colunas: lista de colunas para correlação (None = todas numéricas)
        metodo: 'pearson', 'spearman', 'kendall'
        cmap: colormap do heatmap
        mostrar_valores: mostrar valores de correlação
    """
    plt.figure(figsize=figsize)
    
    # Selecionar colunas
    if colunas is None:
        df_corr = df.select_dtypes(include=[np.number])
    else:
        df_corr = df[colunas]
    
    # Calcular correlação
    corr_matrix = df_corr.corr(method=metodo)
    
    # Heatmap
    sns.heatmap(corr_matrix, 
                annot=mostrar_valores, 
                cmap=cmap, 
                center=0,
                square=True,
                fmt=fmt)
    
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()


def grafico_pairplot(df: pd.DataFrame, colunas=None, categoria=None, 
                    titulo='', figsize=None):
    """
    Pairplot para múltiplas variáveis
    
    Args:
        df: dataframe
        colunas: lista de colunas numéricas
        categoria: coluna categórica para colorir
        titulo: titulo do gráfico
    """
    if colunas:
        df_plot = df[colunas + ([categoria] if categoria else [])]
    else:
        df_plot = df.select_dtypes(include=[np.number])
        if categoria and categoria in df.columns:
            df_plot[categoria] = df[categoria]
    
    if figsize:
        sns.set(rc={'figure.figsize': figsize})
    
    g = sns.pairplot(df_plot, hue=categoria if categoria else None, 
                        diag_kind='hist', plot_kws={'alpha': 0.7})
    
    if titulo:
        g.fig.suptitle(titulo, fontsize=16, y=1.02)
    
    plt.tight_layout()
    plt.show()


def grafico_regressao_multipla(df: pd.DataFrame, x, y, categoria=None,
                                titulo='', figsize=(12, 8)):
    """
    Gráfico de regressão com múltiplas categorias
    """
    if categoria:
        g = sns.lmplot(data=df, x=x, y=y, hue=categoria, 
                        height=6, aspect=1.2)
        g.fig.suptitle(titulo, fontsize=14, y=1.02)
    else:
        plt.figure(figsize=figsize)
        sns.regplot(data=df, x=x, y=y)
        plt.title(titulo, fontsize=14, fontweight='bold')
        plt.tight_layout()
    
    plt.show()