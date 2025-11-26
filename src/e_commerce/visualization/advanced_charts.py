# visualization/advanced_charts.py
"""
Gráficos avançados: subplots, dashboards, séries temporais
Para análises mais complexas e apresentações
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime


def dashboard_basico(df: pd.DataFrame, titulo='Dashboard', figsize=(15, 10)):
    """
    Dashboard com 4 gráficos básicos
    
    Args:
        df: DataFrame com dados
        titulo: título do dashboard
    """
    fig, axes = plt.subplots(2, 2, figsize=figsize)
    fig.suptitle(titulo, fontsize=16, fontweight='bold')
    
    # Selecionar colunas numéricas
    numeric_cols = df.select_dtypes(include=[np.number]).columns[:4]
    
    if len(numeric_cols) >= 2:
        # Gráfico 1: Histograma
        axes[0,0].hist(df[numeric_cols[0]].dropna(), bins=20, alpha=0.7, color='skyblue')
        axes[0,0].set_title(f'Distribuição: {numeric_cols[0]}')
        axes[0,0].grid(True, alpha=0.3)
        
        # Gráfico 2: Box plot
        axes[0,1].boxplot(df[numeric_cols[1]].dropna())
        axes[0,1].set_title(f'Box Plot: {numeric_cols[1]}')
        axes[0,1].grid(True, alpha=0.3)
        
        if len(numeric_cols) >= 3:
            # Gráfico 3: Linha
            axes[1,0].plot(df[numeric_cols[2]].dropna(), marker='o', alpha=0.7)
            axes[1,0].set_title(f'Evolução: {numeric_cols[2]}')
            axes[1,0].grid(True, alpha=0.3)
        
        if len(numeric_cols) >= 4:
            # Gráfico 4: Dispersão
            valid_data = df[[numeric_cols[0], numeric_cols[3]]].dropna()
            axes[1,1].scatter(valid_data[numeric_cols[0]], valid_data[numeric_cols[3]], alpha=0.6)
            axes[1,1].set_xlabel(numeric_cols[0])
            axes[1,1].set_ylabel(numeric_cols[3])
            axes[1,1].set_title(f'Relação: {numeric_cols[0]} vs {numeric_cols[3]}')
            axes[1,1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()



def grafico_linha_temporal(df: pd.DataFrame, x, y, color='blue', linewidth=2, 
                            titulo='', ylabel='', xlabel='', figsize=(12, 6),
                            mostrar_tendencia=False, cor_tendencia='red'):
    """
    Esta função é especializada para gráficos de linha temporais (séries temporais).
    
    Parâmetros:
    df: dataframe
    x: coluna do df com datas/tempo (eixo x)
    y: coluna do df no eixo y (vertical)
    color: cor da linha no gráfico
    linewidth: espessura da linha
    titulo: título do gráfico
    xlabel: rótulo do eixo x
    ylabel: rótulo do eixo y
    figsize: tamanho da figura (largura, altura)
    mostrar_tendencia: adicionar linha de tendência
    cor_tendencia: cor da linha de tendência

    Retorna:
    Gráfico de linha temporal
    """
    plt.figure(figsize=figsize)
    
    # Converter coluna x para datetime se não for
    if not pd.api.types.is_datetime64_any_dtype(df[x]):
        df[x] = pd.to_datetime(df[x])
    
    # Criar o gráfico de linha
    sns.lineplot(data=df, x=x, y=y, 
                color=color, 
                linewidth=linewidth)
    
    # Adicionar linha de tendência se solicitado
    if mostrar_tendencia:
        # Converter datas para números para regressão
        x_numeric = pd.to_numeric(df[x])
        sns.regplot(x=x_numeric, y=df[y], 
                    scatter=False, 
                    line_kws={'color': cor_tendencia, 'linewidth': 2, 'linestyle': '--'})
    
    # Configurar títulos e rótulos
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    
    # Rotacionar rótulos do eixo x para datas
    plt.xticks(rotation=45)
    
    # Configurar grade
    plt.grid(True, linestyle='--', alpha=0.3)
    
    # Melhorar layout
    plt.tight_layout()
    
    # Mostrar gráfico
    plt.show()


def grafico_multiplos_subplots(df: pd.DataFrame, colunas, titulo='',
                                ncols=2, figsize=(15, 10), tipo='linha'):
    """
    Múltiplos subplots para comparar várias variáveis
    
    Args:
        colunas: lista de colunas para plotar
        ncols: número de colunas no grid
        tipo: 'linha', 'hist', 'box'
    """
    n_plots = len(colunas)
    nrows = (n_plots + ncols - 1) // ncols
    
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    fig.suptitle(titulo, fontsize=16, fontweight='bold')
    
    # Garantir que axes seja sempre 2D
    if nrows == 1:
        axes = axes.reshape(1, -1)
    if ncols == 1:
        axes = axes.reshape(-1, 1)
    
    for i, col in enumerate(colunas):
        row = i // ncols
        col_idx = i % ncols
        ax = axes[row, col_idx]
        
        if tipo == 'linha':
            ax.plot(df[col].dropna(), marker='o', alpha=0.7)
        elif tipo == 'hist':
            ax.hist(df[col].dropna(), bins=20, alpha=0.7, color='skyblue')
        elif tipo == 'box':
            ax.boxplot(df[col].dropna())
        
        ax.set_title(f'{tipo.title()}: {col}')
        ax.grid(True, alpha=0.3)
    
    # Remover subplots vazios
    for i in range(n_plots, nrows * ncols):
        row = i // ncols
        col_idx = i % ncols
        fig.delaxes(axes[row, col_idx])
    
    plt.tight_layout()
    plt.show()


def grafico_antes_depois(df: pd.DataFrame, antes_col, depois_col, 
                        identificador=None, titulo='', figsize=(10, 6)):
    """
    Gráfico para comparar valores antes e depois
    
    Args:
        antes_col: coluna com valores antes
        depois_col: coluna com valores depois
        identificador: coluna para identificar cada observação
    """
    plt.figure(figsize=figsize)
    
    if identificador:
        for i in range(len(df)):
            plt.plot([1, 2], [df[antes_col].iloc[i], df[depois_col].iloc[i]], 
                    'o-', alpha=0.6, color='gray', linewidth=1)
    
    # Médias
    media_antes = df[antes_col].mean()
    media_depois = df[depois_col].mean()
    
    plt.plot([1, 2], [media_antes, media_depois], 'ro-', 
                linewidth=3, markersize=10, label='Média')
    
    plt.xlim(0.5, 2.5)
    plt.xticks([1, 2], ['Antes', 'Depois'])
    plt.ylabel('Valores')
    plt.title(titulo or f'Comparação: {antes_col} vs {depois_col}', 
                fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


def heatmap_temporal(df: pd.DataFrame, data_col, valor_col, 
                    titulo='', figsize=(12, 6), freq='M'):
    """
    Heatmap para dados temporais (ex: vendas por mês/ano)
    
    Args:
        freq: frequência de agrupamento ('M', 'D', 'W', 'Y')
    """
    plt.figure(figsize=figsize)
    
    # Converter para datetime
    if not pd.api.types.is_datetime64_any_dtype(df[data_col]):
        df[data_col] = pd.to_datetime(df[data_col])
    
    # Criar pivot table
    df_temp = df.copy()
    df_temp['ano'] = df_temp[data_col].dt.year
    df_temp['mes'] = df_temp[data_col].dt.month
    
    pivot_table = df_temp.pivot_table(values=valor_col, 
                                        index='ano', 
                                        columns='mes', 
                                        aggfunc='mean')
    
    # Heatmap
    sns.heatmap(pivot_table, annot=True, fmt='.1f', cmap='YlOrRd')
    
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.xlabel('Mês')
    plt.ylabel('Ano')
    plt.tight_layout()
    plt.show()