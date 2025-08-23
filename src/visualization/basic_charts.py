"""
Gráficos básicos: barras, linhas, pizza, área
Gráficos fundamentais para análise exploratória
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Gráfico de Barras
def grafico_barra(df: pd.DataFrame, x, y, hue=None, orient: str = 'v', paleta='tab10', titulo='', ylabel='', xlabel=''):
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
    plt.figure(figsize=(12,8))

    ax = sns.barplot(data=df, x=x, y=y, hue=hue, palette=paleta, orient=orient)
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
def grafico_linha(df: pd.DataFrame, x=None, y=None, hue=None, 
                    color='blue', linewidth=2, linestyle='-', 
                    marker='o', markersize=6, titulo='', ylabel='', xlabel='', 
                    alpha=0.8, figsize=(10, 6), grid=True, 
                    ytick=False, xticks_step=None, xrotaion=45):
    """
    Gera gráfico de linha:
    - x e y devem ser nomes de colunas (str).
    - xticks_step: controla o espaçamento dos ticks do eixo X (int).
    """
    plt.figure(figsize=figsize)

    # Converte Period para datetime automaticamente
    if pd.api.types.is_period_dtype(df[x]):
        df[x] = df[x].dt.to_timestamp()

    # 🔹 Gráfico de linha
    sns.lineplot(data=df, x=x, y=y, hue=hue,
                    color=color, linewidth=linewidth,
                    linestyle=linestyle, marker=marker,
                    markersize=markersize, alpha=alpha)

    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    
    if grid:
        plt.grid(True, linestyle='--', alpha=0.3)
    
    if ytick:
        plt.yticks([])  
        plt.gca().set_yticklabels([])

    # 🔹 Controla os ticks do eixo X
    if xticks_step is not None:
        plt.xticks(df[x][::xticks_step])  # pega de step em step
    
    plt.xticks(rotation=xrotaion)

    plt.tight_layout()
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
    Gráfico de pizza melhorado: lida com fatias pequenas.
    """
    plt.figure(figsize=figsize)

    if colors is None:
        colors = plt.cm.Set3.colors

    # Calcular explode para fatias pequenas
    explode = [0.05 if v < 0.05*df[values].sum() else 0 for v in df[values]]

    wedges, texts, autotexts = plt.pie(
        df[values],
        labels=df[labels],
        autopct=autopct,
        startangle=90,
        colors=colors,
        explode=explode,
        pctdistance=0.7,     # afasta percentual do centro
        labeldistance=1.05   # afasta label do centro
    )

    # Ajustar fonte dos labels e percentuais
    for t in texts:
        t.set_fontsize(10)
    for at in autotexts:
        at.set_fontsize(9)

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

# Frequência
def grafico_frequencia(df: pd.DataFrame, coluna, titulo='', xlabel='', ylabel='Contagem', 
                        figsize=(10,6), paleta='tab10', rot=0):
    """
    Gráfico de barras mostrando a frequência (count) de uma coluna categórica.
    
    Args:
        df: DataFrame com os dados.
        coluna: coluna categórica para contar frequência.
        titulo: título do gráfico.
        xlabel: rótulo do eixo x.
        ylabel: rótulo do eixo y (default: 'Contagem').
        figsize: tamanho da figura.
        paleta: paleta de cores (Seaborn).
        rot: rotação dos labels do eixo x.
    """
    plt.figure(figsize=figsize)
    ax = sns.countplot(data=df, x=coluna, palette=paleta, hue= coluna, order=df[coluna].value_counts().index)
    
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel if xlabel else coluna, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.xticks(rotation=rot)
    
    # Colocar contagem no topo das barras
    for p in ax.patches:
        height = p.get_height()
        ax.annotate(f'{height}', xy=(p.get_x() + p.get_width() / 2, height),
                    ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    plt.show()
