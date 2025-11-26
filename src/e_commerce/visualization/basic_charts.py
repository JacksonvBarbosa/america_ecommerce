"""
Gráficos básicos: barras, linhas, pizza, área
Gráficos fundamentais para análise exploratória
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Gráfico de Barras
def grafico_barra(df: pd.DataFrame, x, y, hue=None, orient: str = 'v', figsize=(10,6),
                  paleta='tab10', cores=None, titulo='', ylabel='', xlabel='', errorbar=None,
                  grid: bool = False, alpha=None, legend_title: str = None, legend_labels: dict = None):
    """
    Função para gerar gráfico de barras com Seaborn.

    Parâmetros:
    df: DataFrame
    x: coluna do df no eixo x (string)
    y: coluna do df no eixo y (string)
    hue: coluna para agrupar categorias (string ou None)
    orient: 'v' = vertical, 'h' = horizontal
    paleta: paleta de cores (se cores=None)
    cores: lista de cores para personalização manual
    titulo: título do gráfico
    xlabel: rótulo do eixo x
    ylabel: rótulo do eixo y
    grid: mostrar grid (True/False)
    alpha: transparência da grid
    legend_title: título da legenda (aplica se hue não for None)
    legend_labels: dict -> {'1':'Masculino', '2':'Feminino'} ou {'M':'Masculino', 'F':'Feminino'}
    """

    plt.figure(figsize=figsize)

    # Se hue existe, usa cores ou paleta
    if hue is not None:
        if cores is not None:
            ax = sns.barplot(data=df, x=x, y=y, hue=hue, palette=cores, orient=orient, errorbar=errorbar)
        else:
            ax = sns.barplot(data=df, x=x, y=y, hue=hue, palette=paleta, orient=orient, errorbar=errorbar)
    else:
        if cores is not None:
            ax = sns.barplot(data=df, x=x, y=y, palette=cores, orient=orient, errorbar=errorbar)
        else:
            ax = sns.barplot(data=df, x=x, y=y, orient=orient, errorbar=errorbar)

    plt.title(titulo, fontsize=18, fontweight='bold', loc='left')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(rotation=360)

    # Ajuste dos limites
    if orient == 'v':
        y_limite = df[y].max()
        plt.ylim(0, y_limite * 1.1)
    else:
        x_limite = df[x].max()
        plt.xlim(0, x_limite * 1.1)

    # Labels das barras
    for container in ax.containers:
        ax.bar_label(container, label_type='edge', fontsize=11, fontweight='bold', padding=3)

    # Grid (aplica apenas se grid=True)
    if grid:
        plt.grid(True, alpha=alpha if alpha is not None else 0.3)

    if hue is not None:
        handles, labels = ax.get_legend_handles_labels()
        
        # Só cria legenda se tiver labels válidos
        if labels and not all(l.startswith("_") for l in labels):
            if legend_labels:
                labels = [legend_labels.get(l, l) for l in labels]
            ax.legend(handles=handles, labels=labels, title=legend_title)

    plt.tight_layout()
    plt.show()


# Gráfico de barras multiplos
def grafico_barra_multicol(df: pd.DataFrame, x, colunas_y: list, hue=None, orient='v', figsize=(12,6),
                            paleta='tab10', titulo='', ylabel='', xlabel='', errorbar=None,
                            grid=False, alpha=None, legend_title=None, legend_labels=None):
    """
    Gráfico de barras para múltiplas colunas.
    colunas_y = ['col1', 'col2', 'col3', 'col4', 'col5']
    colunas_y: lista de colunas numéricas do df que serão plotadas
    """
    # Transformar de wide para long
    df_long = df.melt(id_vars=[x], value_vars=colunas_y, var_name='variavel', value_name='valor')
    
    plt.figure(figsize=figsize)
    
    if hue is not None:
        ax = sns.barplot(data=df_long, x=x, y='valor', hue=hue, palette=paleta, orient=orient, errorbar=errorbar)
    else:
        ax = sns.barplot(data=df_long, x=x, y='valor', hue='variavel', palette=paleta, orient=orient, errorbar=errorbar)
    
    plt.title(titulo, fontsize=18, fontweight='bold', loc='left')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(rotation=45)
    
    # Labels das barras
    for container in ax.containers:
        ax.bar_label(container, label_type='edge', padding=3)
    
    # Grid
    if grid:
        plt.grid(True, alpha=alpha if alpha else 0.3)
    
    if hue is None:
        handles, labels = ax.get_legend_handles_labels()
        if labels:
            if legend_labels:
                labels = [legend_labels.get(l, l) for l in labels]
            ax.legend(handles=handles, labels=labels, title=legend_title)
    
    plt.tight_layout()
    plt.show()

# Gráfico de Barras empilhadas
'''def grafico_barra_empilhada(df: pd.DataFrame, x, y, hue=None, orient: str = 'v',
                            figsize=(10,6), paleta='tab10', cores=None,
                            titulo='', xlabel='', ylabel='', grid: bool = False,
                            alpha=None, legend_title: str = None, legend_labels: dict = None):
    """
    Função para gerar gráfico de barras empilhadas com Matplotlib + Pandas.

    Parâmetros:
    df: DataFrame
    x: coluna no eixo x
    y: coluna com valores numéricos
    hue: coluna para categorias que serão empilhadas
    orient: 'v' = vertical, 'h' = horizontal
    paleta: paleta de cores (usada se cores=None)
    cores: lista de cores definidas manualmente (opcional)
    titulo: título do gráfico
    xlabel: rótulo do eixo x
    ylabel: rótulo do eixo y
    grid: mostrar grid (True/False)
    alpha: transparência da grid
    legend_title: título da legenda
    legend_labels: dict para renomear categorias da legenda
    """

    # Preparar dados pivotados
    tabela = df.pivot_table(index=y if orient=='h' else x,
                            columns=hue,
                            values=x if orient=='h' else y,
                            aggfunc='sum',
                            fill_value=0)

    # Definir cores
    if cores is not None:
        # Se usuário passou lista de cores
        cores_final = cores
    else:
        # Caso contrário, pega da paleta escolhida
        cores_final = plt.get_cmap(paleta).colors[:len(tabela.columns)]

    fig, ax = plt.subplots(figsize=figsize)

    if orient == 'v':
        tabela.plot(kind='bar', stacked=True, color=cores_final, ax=ax)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
    else:
        tabela.plot(kind='barh', stacked=True, color=cores_final, ax=ax)
        ax.set_ylabel(ylabel)
        ax.set_xlabel(xlabel)

    # Adicionar labels dentro das barras
    for container in ax.containers:
        ax.bar_label(container, label_type='center', fontsize=11, fontweight='bold', color="white")

    # Título
    ax.set_title(titulo, fontsize=18, fontweight='bold', loc='left')

    # Grid
    if grid:
        ax.grid(True, alpha=alpha if alpha is not None else 0.3)

    # Legenda
    handles, labels = ax.get_legend_handles_labels()
    if legend_labels:
        labels = [legend_labels.get(l, l) for l in labels]
    ax.legend(handles, labels, title=legend_title)

    plt.tight_layout()
    plt.show()'''

# Gráfico de Barras empilhadas
def grafico_barra_empilhada(df: pd.DataFrame, x, y, hue=None, orient: str = 'v',
                            figsize=(10,6), paleta='tab10', cores=None,
                            titulo='', xlabel='', ylabel='', grid: bool = False,
                            alpha=None, legend_title: str = None, legend_labels: dict = None,
                            mostrar_proporcao: bool = False, despine_top=None, despine_right=None, cor_label: str = "Grey"):
    """
    Função para gerar gráfico de barras empilhadas com Matplotlib + Pandas.

    Parâmetros:
    df: DataFrame
    x: coluna no eixo x
    y: coluna com valores numéricos
    hue: coluna para categorias que serão empilhadas
    orient: 'v' = vertical, 'h' = horizontal
    paleta: paleta de cores (usada se cores=None)
    cores: lista de cores definidas manualmente (opcional)
    titulo: título do gráfico
    xlabel: rótulo do eixo x
    ylabel: rótulo do eixo y
    grid: mostrar grid (True/False)
    alpha: transparência da grid
    legend_title: título da legenda
    legend_labels: dict para renomear categorias da legenda
    mostrar_proporcao: exibir também a porcentagem ao lado do valor absoluto
    cor_label: cor do texto dentro das barras (default = branco)
    """

    # Preparar dados pivotados
    tabela = df.pivot_table(index=y if orient=='h' else x,
                            columns=hue,
                            values=x if orient=='h' else y,
                            aggfunc='sum',
                            fill_value=0)

    # Definir cores
    if cores is not None:
        cores_final = cores
    else:
        cores_final = plt.get_cmap(paleta).colors[:len(tabela.columns)]

    fig, ax = plt.subplots(figsize=figsize)

    if orient == 'v':
        tabela.plot(kind='bar', stacked=True, color=cores_final, ax=ax)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
    else:
        tabela.plot(kind='barh', stacked=True, color=cores_final, ax=ax)
        ax.set_ylabel(ylabel)
        ax.set_xlabel(xlabel)

    # Adicionar labels dentro ou fora das barras
    totais = tabela.sum(axis=1)

    for container, col in zip(ax.containers, tabela.columns):
        for bar, valor, total in zip(container, tabela[col], totais):
            if valor > 0:
                if mostrar_proporcao:
                    proporcao = (valor / total) * 100
                    texto = f"{int(valor)} ({proporcao:.1f}%)"
                else:
                    texto = f"{int(valor)}"

                if orient == 'v':
                    largura = bar.get_height()
                    xpos = bar.get_x() + bar.get_width()/2
                    ypos = bar.get_y() + bar.get_height()/2
                    # Se a barra for muito pequena, joga o texto acima da barra
                    if largura < total * 0.15:  
                        ax.text(xpos, bar.get_y() + bar.get_height() + (total*0.02),
                                texto, ha='center', va='bottom',
                                fontsize=10, fontweight='bold', color="black")
                    else:
                        ax.text(xpos, ypos, texto,
                                ha='center', va='center',
                                fontsize=10, fontweight='bold', color=cor_label)
                else:  # horizontal
                    largura = bar.get_width()
                    xpos = bar.get_x() + bar.get_width()/2
                    ypos = bar.get_y() + bar.get_height()/2
                    if largura < total * 0.10:  
                        ax.text(bar.get_x() + bar.get_width() + (total*0.02), ypos,
                                texto, ha='left', va='center',
                                fontsize=10, fontweight='bold', color=cor_label)
                    else:
                        ax.text(xpos, ypos, texto,
                                ha='center', va='center',
                                fontsize=10, fontweight='bold', color=cor_label)

    # Título
    ax.set_title(titulo, fontsize=18, fontweight='bold', loc='left')

    # Grid
    if grid:
        ax.grid(True, alpha=alpha if alpha is not None else 0.3)

    # Legenda
    handles, labels = ax.get_legend_handles_labels()
    if legend_labels:
        labels = [legend_labels.get(l, l) for l in labels]
    ax.legend(handles, labels, title=legend_title)

    sns.despine(top=despine_top, right=despine_right)
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