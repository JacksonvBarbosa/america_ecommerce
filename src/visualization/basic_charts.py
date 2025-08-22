"""
Gráficos básicos: barras, linhas, pizza, área
Gráficos fundamentais para análise exploratória
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Gráfico de Barras
def grafico_barra(df: pd.DataFrame, x, y, hue, orient: str = 'v', paleta='tab10', titulo='', ylabel='', xlabel=''):
    """
    Esta função recebe parametros para gerar gráfico de barra.
    
    Parâmetros:
    df: dataframe
    x: coluna do df no eixo x (horizontal)
    y: coluna do df no eixo y (vertical)
    hue: para agrupar os dados categoricas e atribuir cores diferentes a elas
    titulo: titulo do gráfico
    xlabel: rótulo do eixo x
    ylabel: rótulo do eixo y

    Retorna:
    Gráfico de barras (barplot)
    """
    plt.figure(figsize=(10,6))

    ax = sns.barplot(df, x=x,y=y,hue=hue , palette=paleta, orient=orient)
    plt.title(titulo, fontsize=18, fontweight='bold', loc='left')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(rotation=360)

    y_limite = y.max()
    plt.ylim(0, y_limite * 1.1)

    for container in ax.containers:
        ax.bar_label(container, label_type='edge', padding=3)

    plt.tight_layout()
    plt.show()

# Gráfico de Linha
def grafico_linha(df: pd.DataFrame, x, y, hue= None, color='blue', linewidth=2, linestyle='-', 
                    marker='o', markersize=6, titulo='', ylabel='', xlabel='', 
                    alpha=0.8, figsize=(10, 6), grid=True):
    """
    Esta função recebe parâmetros para gerar gráfico de linha.
    
    Parâmetros:
    df: dataframe
    x: coluna do df no eixo x (horizontal)
    y: coluna do df no eixo y (vertical)
    color: cor da linha no gráfico
    linewidth: espessura da linha
    linestyle: estilo da linha ('-', '--', '-.', ':')
    marker: marcador dos pontos ('o', 's', '^', 'D', etc.)
    markersize: tamanho dos marcadores
    titulo: título do gráfico
    xlabel: rótulo do eixo x
    ylabel: rótulo do eixo y
    alpha: transparência da linha
    figsize: tamanho da figura (largura, altura)
    grid: mostrar grade no gráfico

    Retorna:
    Gráfico de linha (lineplot)
    """
    plt.figure(figsize=figsize)
    
    # Criar o gráfico de linha
    sns.lineplot(data=df, x=x, y=y, hue=hue,
                color=color, 
                linewidth=linewidth,
                linestyle=linestyle,
                marker=marker,
                markersize=markersize,
                alpha=alpha)
    
    # Configurar títulos e rótulos
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    
    # Configurar grade
    if grid:
        plt.grid(True, linestyle='--', alpha=0.3)
    
    # Melhorar layout
    plt.tight_layout()
    
    # Mostrar gráfico
    plt.show()

# Gráfico Multiplas Linhas
def grafico_multiplas_linhas(df: pd.DataFrame, x, y_columns, colors=None, linewidth=2, 
                            linestyle='-', marker='o', markersize=6, titulo='', 
                            ylabel='', xlabel='', alpha=0.8, figsize=(12, 6), 
                            grid=True, legend=True):
    """
    Esta função recebe parâmetros para gerar gráfico com múltiplas linhas.
    
    Parâmetros:
    df: dataframe
    x: coluna do df no eixo x (horizontal)
    y_columns: lista com nomes das colunas para múltiplas linhas
    colors: lista de cores para cada linha (opcional)
    linewidth: espessura da linha
    linestyle: estilo da linha ('-', '--', '-.', ':')
    marker: marcador dos pontos ('o', 's', '^', 'D', etc.)
    markersize: tamanho dos marcadores
    titulo: título do gráfico
    xlabel: rótulo do eixo x
    ylabel: rótulo do eixo y
    alpha: transparência das linhas
    figsize: tamanho da figura (largura, altura)
    grid: mostrar grade no gráfico
    legend: mostrar legenda

    Retorna:
    Gráfico com múltiplas linhas
    """
    plt.figure(figsize=figsize)
    
    # Cores padrão se não especificadas
    if colors is None:
        colors = plt.cm.Set1(range(len(y_columns)))
    
    # Plotar cada linha
    for i, col in enumerate(y_columns):
        color = colors[i] if i < len(colors) else f'C{i}'
        
        sns.lineplot(data=df, x=x, y=col,
                    color=color,
                    linewidth=linewidth,
                    linestyle=linestyle,
                    marker=marker,
                    markersize=markersize,
                    alpha=alpha,
                    label=col)
    
    # Configurar títulos e rótulos
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    
    # Configurar legenda
    if legend:
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Configurar grade
    if grid:
        plt.grid(True, linestyle='--', alpha=0.3)
    
    # Melhorar layout
    plt.tight_layout()
    
    # Mostrar gráfico
    plt.show()

# Pizza
def grafico_pizza(df: pd.DataFrame, values, labels, titulo='', figsize=(8, 8), 
                    autopct='%1.1f%%', colors=None):
    """
    Gráfico de pizza
    
    Args:
        values: coluna com valores
        labels: coluna com rótulos
        autopct: formato dos percentuais
    """
    plt.figure(figsize=figsize)
    
    if colors is None:
        colors = plt.cm.Set3.colors
    
    plt.pie(df[values], labels=df[labels], autopct=autopct, 
            colors=colors, startangle=90)
    
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

# Área
def grafico_area(df: pd.DataFrame, x, y, color='lightblue', alpha=0.7, 
                    titulo='', ylabel='', xlabel='', figsize=(10, 6)):
    """
    Gráfico de área
    """
    plt.figure(figsize=figsize)
    
    plt.fill_between(df[x], df[y], color=color, alpha=alpha)
    plt.plot(df[x], df[y], color='navy', linewidth=2)
    
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel or x, fontsize=12)
    plt.ylabel(ylabel or y, fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()