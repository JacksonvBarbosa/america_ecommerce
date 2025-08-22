import os

def find_project_root(marker_folder="src"):
    """
    Encontra a raiz do projeto subindo a hierarquia até encontrar a pasta indicada.
    """
    current = os.path.abspath(os.getcwd())
    while True:
        if marker_folder in os.listdir(current):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            raise RuntimeError(f"❌ Pasta '{marker_folder}' não encontrada na hierarquia.")
        current = parent

# Diretório base do projeto (sempre a raiz, mesmo rodando de subpastas)
BASE_DIR = find_project_root("src")

# Estrutura de pastas para dados
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_RAW = os.path.join(DATA_DIR, "raw")
DATA_PROCESSED = os.path.join(DATA_DIR, "processed")
DATA_INTERIM = os.path.join(DATA_DIR, "interim")

# Pasta principal de notebooks
NOTEBOOK_DIR = os.path.join(BASE_DIR, "notebook")
