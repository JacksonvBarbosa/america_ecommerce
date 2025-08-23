import os
import pandas as pd
from src.config import DATA_RAW, DATA_PROCESSED

def extract_csv_raw(filename_or_path: str, sep: str = ',') -> pd.DataFrame:
    """
    Lê CSV da pasta DATA_RAW ou de um caminho absoluto.
    """
    filepath = filename_or_path if os.path.isabs(filename_or_path) else os.path.join(DATA_RAW, filename_or_path)
    return pd.read_csv(filepath, sep=sep)

def extract_csv_processed(filename_or_path: str, sep: str = ',', parse_dates: str= None) -> pd.DataFrame:
    """
    Lê CSV da pasta DATA_PROCESSED ou de um caminho absoluto.
    """
    filepath = filename_or_path if os.path.isabs(filename_or_path) else os.path.join(DATA_PROCESSED, filename_or_path)
    return pd.read_csv(filepath, sep=sep, parse_dates=parse_dates)
