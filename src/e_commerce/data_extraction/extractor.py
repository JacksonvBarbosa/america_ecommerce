from e_commerce.data_extraction.csv_extraction import (
    extract_csv_raw,
    extract_csv_interim,
    extract_csv_processed,
)
from e_commerce.data_extraction.excel_extraction import (
    extract_excel_raw,
    extract_excel_interim,
    extract_excel_processed,
)
from e_commerce.data_extraction.json_extraction import (
    extract_json_raw,
    extract_json_interim,
    extract_json_processed,
)
from e_commerce.data_extraction.parquet_extraction import (
    extract_parquet_raw,
    extract_parquet_interim,
    extract_parquet_processed,
)

from e_commerce.data_extraction.api_extraction import (
    extract_from_api,
    extract_from_rest_api
)

from e_commerce.data_extraction.database_extraction import (
    extract_from_sqlite,
    extract_from_database,
    extract_table_from_database
)


def get_data(source_type: str, type_name: str = None, **kwargs):
    """
    Orquestrador de extração de dados.
    
    Args:
        source_type (str): tipo da fonte ("csv", "excel", "json", "parquet", "xml", "api", "db", "web")
        type_name (str, opcional): camada de dados ("raw", "processed", "interim") 
                                    - obrigatório para csv, excel, json, parquet, xml
                                    - ignorado para api, db e web
        **kwargs: parâmetros extras para a função de extração (ex.: file_name, url, query, connection_string, css_selector) - passe filename_or_path
    
    Returns:
        DataFrame ou objeto retornado pela função de extração
    """
    # Fontes que possuem camadas (raw, processed, interim)
    if source_type == "csv":
        if type_name == "raw":
            return extract_csv_raw(**kwargs)
        elif type_name == "processed":
            return extract_csv_processed(**kwargs)
        elif type_name == "interim":
            return extract_csv_interim(**kwargs)
        else:
            raise ValueError(f"Tipo de CSV inválido: {type_name}")

    elif source_type == "excel":
        if type_name == "raw":
            return extract_excel_raw(**kwargs)
        elif type_name == "processed":
            return extract_excel_processed(**kwargs)
        elif type_name == "interim":
            return extract_excel_interim(**kwargs)
        else:
            raise ValueError(f"Tipo de Excel inválido: {type_name}")

    elif source_type == "json":
        if type_name == "raw":
            return extract_json_raw(**kwargs)
        elif type_name == "processed":
            return extract_json_processed(**kwargs)
        elif type_name == "interim":
            return extract_json_interim(**kwargs)
        else:
            raise ValueError(f"Tipo de JSON inválido: {type_name}")

    elif source_type == "parquet":
        if type_name == "raw":
            return extract_parquet_raw(**kwargs)
        elif type_name == "processed":
            return extract_parquet_processed(**kwargs)
        elif type_name == "interim":
            return extract_parquet_interim(**kwargs)
        else:
            raise ValueError(f"Tipo de Parquet inválido: {type_name}")

    # APIs
    elif source_type == "api":
        if "base_url" in kwargs and "endpoint" in kwargs:
            return extract_from_rest_api(**kwargs)
        elif "url" in kwargs:
            return extract_from_api(**kwargs)
        else:
            raise ValueError("Para API, forneça 'url' ou 'base_url' + 'endpoint'.")

    # Banco de dados
    elif source_type == "db":
        if "database_path" in kwargs:
            return extract_from_sqlite(**kwargs)
        elif "connection_string" in kwargs and "query" in kwargs:
            return extract_from_database(**kwargs)
        elif "table_name" in kwargs and "connection_string" in kwargs:
            return extract_table_from_database(**kwargs)
        else:
            raise ValueError("Para DB, forneça 'database_path', ou 'connection_string' + 'query', ou 'table_name' + 'connection_string'.")

    else:
        raise ValueError(f"Fonte de dados não suportada: {source_type}")
