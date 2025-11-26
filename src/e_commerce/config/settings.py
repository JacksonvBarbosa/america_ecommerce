# import os

# # Caminho da pasta onde este arquivo está (nome porjeto/)
# PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

# # Raiz do projeto (um nível acima de src/)
# BASE_DIR = os.path.dirname(os.path.dirname(PACKAGE_DIR))

# # Estrutura de pastas para dados
# DATA_DIR = os.path.join(BASE_DIR, "data")
# DATA_RAW = os.path.join(DATA_DIR, "raw")
# DATA_PROCESSED = os.path.join(DATA_DIR, "processed")
# DATA_INTERIM = os.path.join(DATA_DIR, "interim")

from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent
BASE_DIR = PACKAGE_DIR.parent.parent.parent

DATA_DIR = BASE_DIR / "data"
DATA_RAW = DATA_DIR / "raw"
DATA_PROCESSED = DATA_DIR / "processed"
DATA_INTERIM = DATA_DIR / "interim"
