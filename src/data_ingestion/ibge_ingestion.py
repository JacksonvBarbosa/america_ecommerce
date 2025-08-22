import os
import requests
from src.config import DATA_RAW
from src.data_extraction.json_extraction import extract_json_raw

def download_from_ibge(endpoint: str, filename: str = "ibge_data.json"):
    """
    Baixa dados JSON da API do IBGE e salva na pasta DATA_RAW.
    """
    url = f"https://servicodados.ibge.gov.br/api/v3/{endpoint}"
    print(f"📥 Baixando dados do IBGE: {url}")
    response = requests.get(url)

    if response.status_code == 200:
        filepath = os.path.join(DATA_RAW, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"✅ Dados salvos em: {filepath}")
        return extract_json_raw(filename)
    else:
        raise ConnectionError(f"Falha ao acessar {url} - Status: {response.status_code}")
