# Análise da Qualidade de Vinhos
**Portfólio de Data Analytics | Jackson dos Santos Ventura**

## 📊 Projeto: Análise Exploratória e-commerce

### Contexto do Projeto


### Objetivo


## 🔬 Metodologia

### 1. Aquisição e Preparação dos Dados
**Dataset:** 

**Ferramentas:** Python, Pandas, NumPy, Matplotlib, Seaborn

**Procedimentos:**
- Importação e inspeção inicial do dataset
- Tratamento de valores duplicados e ausentes
- Ajuste de tipos de dados
- Criação de funções modulares para extração, transformação e armazenamento de dados no pacote `etl/`
- Implementação de tratamento de outliers e balanceamento de classes no pacote `features/`

### 2. Análise Exploratória de Dados (EDA)
- Visualização e análise de distribuições de variáveis químicas
- Identificação de correlações entre variáveis e qualidade do vinho
- Uso de gráficos de dispersão, boxplots, histogramas e mapas de calor
- Criação do módulo `visualization/` para centralizar funções gráficas reutilizáveis

### 3. Desenvolvimento de Modelos de Machine Learning
- Estrutura de código organizada em pacotes reutilizáveis (`models/`) para classificação, regressão e clustering
- Implementação de pipelines (`pipeline_classification.py`, `pipeline_regression.py`, `pipeline_clustering.py`) para padronizar o fluxo de treino e avaliação
- Utilização do `model_factory.py` com lazy loading, permitindo carregar modelos sob demanda e melhorar a escalabilidade do projeto
- Aplicação de técnicas de otimização de hiperparâmetros com RandomizedSearchCV
- Avaliação de modelos utilizando métricas como Acurácia, Precisão, Recall, F1-score e ROC AUC

### 4. Modularização e Escalabilidade
- Estrutura do projeto planejada para reuso e manutenção em diferentes datasets
- Separação de responsabilidades por pacotes:
  - `etl/` → Funções de extração, transformação e armazenamento
  - `features/` → Engenharia de variáveis e tratamento de dados
  - `models/` → Treinamento, avaliação e pipelines de ML
  - `visualization/` → Geração de gráficos e plots
- Suporte para inclusão de novos modelos no `model_factory.py` sem alteração no restante do código

### 5. Armazenamento e Versionamento de Modelos
- Modelos treinados salvos em `models_storage/` para reutilização futura
- Uso de joblib para serialização
- Versionamento do código via GitHub

## 📊 Análise Exploratória e Pré-Processamento — Qualidade de Vinhos

Este estudo tem como objetivo analisar o Wine Quality Dataset, obtido através do Kaggle, e aplicar técnicas de pré-processamento para preparar os dados para modelos de machine learning voltados à previsão da qualidade de vinhos.

### 1. Entendimento Inicial dos Dados
O dataset foi analisado em sua forma bruta (raw data), contendo atributos físico-químicos e a nota de qualidade do vinho.

A partir das estatísticas descritivas, identificamos:
- Alta dispersão na maioria das variáveis, devido ao alto desvio padrão


### 2. Dados Duplicados
Não há registros duplicados no DataFrame.

### 3. Distribuição e Outliers
Os gráficos de distribuição e boxplots mostraram:


### 4. Relações Entre Variáveis



### 5. Balanceamento de Classes


### 6. Conclusões e Próximos Passos


## 🤖 Machine Learning


### 🔹 Modelos utilizados

#### Classificação
- `logistic_regression` → log_reg
- `random_forest` → rf_clf
- `xgboost` → xgb_clf
- `lightgbm` → lgbm_clf
- `catboost` → catb_clf
- `tree_classifier` → treec_clf
- `svm_classifier` → svm_clf

#### Regressão
- `linear_regression` → lin_reg
- `random_forest` → rf_reg
- `xgboost` → xgb_reg
- `lightgbm` → lgbm_reg

#### Clustering
- `kmeans` → kmeans_cluster
- `dbscan` → dbscan_cluster

Nosso modelo base, a **Árvore de Classificação**, já apresentou um resultado muito satisfatório, como mostrado anteriormente. A partir dele, rodamos outros modelos para comparação e aplicamos validações para garantir que nossos dados não estivessem sofrendo de overfitting, o que poderia prejudicar as previsões.

### 📊 Comparação de Modelos
- **Regressão Logística** → 
- **Todos os modelos** → Obtiveram F1-score acima de 
- **Melhor desempenho** → Random Forest, 

### 🔍 Validações Realizadas

#### 1. Validação Cruzada + Random Search
Foi aplicada validação cruzada combinada com Random Search, que testa diferentes blocos de dados separadamente, preservando a generalização.

**Resultados:**
- Média dos scores por fold: 
- Desvio padrão:  (baixo, indicando consistência)
- Resultado de acurácia

#### 2. Análise de Overfitting


### ✅ Conclusão
Os testes e validações confirmaram que o **modelo** é o modelo mais adequado para este problema, entregando alta performance e mantendo a capacidade de generalização. O próximo passo será aplicar este modelo em dados novos para validar seu comportamento em produção.

## 🚀 Como utilizar no projeto

A arquitetura do projeto foi pensada para ser prática. Para treinar, avaliar e fazer previsões com qualquer modelo disponível, siga o guia abaixo.

### 1. Instalação e Configuração
Para replicar o ambiente de desenvolvimento conda, siga estes passos:

**Crie e ative o ambiente virtual conda:**
```bash
# Cria o ambiente e já instala as dependências do projeto
conda env create -f environment.yml

# Ative o ambiente
conda activate <nome do projeto>

# caso não saiba entre em enviroment que o nome estará lá
```


**Configure no VS Code:**
1. Pressione `Ctrl + Shift + P`
2. Digite "Python: Select Interpreter"
3. Escolha o ambiente que você criou

### 2. Exemplo de uso com o pipeline_classification
A forma mais prática de testar um modelo é utilizando a função de pipeline. Basta fornecer o caminho do seu arquivo de dados e o nome do modelo desejado.

```python
from src.models.pipeline_classification import pipeline_classification

# Exemplo de uso para o modelo RandomForest
results = pipeline_classification(
    data_path=DATA_PROCESSED / 'seu_dataset_processado.csv',
    target_column='qualidade',
    model_name='random_forest',
    scale_type='standard',
    test_size=0.2
)

# Para inspecionar os resultados
print("Métricas de Avaliação:", results['metrics'])
print("Modelo Treinado:", results['model'])
```

### 3. Testes individuais
Para testar um modelo específico sem usar o pipeline completo, você pode criar e treinar diretamente:

```python
from src.models.model_factory import ModelFactory

# Carregar o modelo desejado
modelo = ModelFactory.create_classification_model("random_forest")

# Treinar e usar o modelo
modelo.fit(X_train, y_train)
predicoes = modelo.predict(X_test)
```

## 📚 Referências

- **UCI Machine Learning Repository** - Wine Quality Dataset

- **Winefun** - "Acidez volátil: conheça um dos defeitos mais controvertidos do mundo dos vinhos"  
  Fonte: Winefun  
  https://winefun.com.br/acidez-volatil-conheca-um-dos-defeitos-mais-controvertidos-do-mundo-dos-vinhos/

- **Wine.com.br** - Winepedia: "Álcool pra quê?"  
  https://www.wine.com.br/winepedia/alcool-pra-que/

---

*Este projeto faz parte do meu portfólio em desenvolvimento durante a pós-graduação em Data Analytics. À medida que avanço no curso, novas técnicas e análises serão incorporadas para enriquecer este e outros estudos.*