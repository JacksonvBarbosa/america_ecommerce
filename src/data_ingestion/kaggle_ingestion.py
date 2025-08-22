import os
import shutil
import kagglehub
from src.config import DATA_RAW

def download_from_kaggle(dataset: str, sep: str = ','):
    """
    Baixa dataset do Kaggle e salva todos os arquivos CSV na pasta DATA_RAW.
    Não retorna DataFrame — apenas salva os arquivos.
    """
    print(f"📥 Baixando dataset '{dataset}' do Kaggle...")
    kaggle_path = kagglehub.dataset_download(dataset)

    csv_count = 0
    for root, _, files in os.walk(kaggle_path):
        for file in files:
            if file.endswith(".csv"):
                # Padroniza nome: minúsculas e underscores
                clean_name = file.lower().replace(" ", "_").replace("-", "_")

                source_path = os.path.join(root, file)
                dest_path = os.path.join(DATA_RAW, clean_name)

                shutil.copy(source_path, dest_path)
                print(f"✅ Arquivo copiado para: {dest_path}")
                csv_count += 1

    if csv_count == 0:
        raise FileNotFoundError("Nenhum arquivo CSV encontrado no dataset Kaggle.")

    print(f"📦 {csv_count} arquivos CSV salvos em {DATA_RAW}")
