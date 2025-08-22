import os
import boto3
from src.config import DATA_RAW
from src.data_extraction.csv_extraction import extract_csv_raw

def download_from_s3(bucket: str, file_key: str, aws_access_key_id: str, aws_secret_access_key: str):
    """
    Baixa arquivo do Amazon S3 e salva na pasta DATA_RAW.
    """
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    dest_path = os.path.join(DATA_RAW, os.path.basename(file_key))
    print(f"📥 Baixando {file_key} do bucket {bucket}...")
    s3.download_file(bucket, file_key, dest_path)
    print(f"✅ Arquivo salvo em: {dest_path}")

    return extract_csv_raw(os.path.basename(file_key))
