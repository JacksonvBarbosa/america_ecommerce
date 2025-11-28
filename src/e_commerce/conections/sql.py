# Libs
from sqlalchemy import create_engine, text
import sys

# Testar a conexão ao banco de dados
# def test_connection(engine, schema):

#     try:
#         with engine.connect() as connection:
            
#             # Testar a versão do PostgreSQL
#             result = connection.execute(text("SELECT version();"))
#             versao = result.fetchone()
#             print("✅ Conectado com sucesso:", versao[0])

#             # Listar as tabelas no schema público
#             result = connection.execute(text("""
#                 SELECT table_name
#                 FROM information_schema.tables
#                 WHERE table_schema = 'public';
#             """))
#             tabelas = result.fetchall()
#             print("📄 Tabelas no banco:")
#             for tabela in tabelas:
#                 print("-", tabela[0])

#     except Exception as e:
#         print("❌ Erro ao executar comandos:", e)
#         sys.exit()


def test_connection(engine, schema):
    try:
        with engine.connect() as conn:
            # Setar o schema desejado
            conn.execute(text(f'SET search_path TO "{schema}";'))
            # Teste simples
            versao = conn.execute(text("SELECT version();")).fetchone()
            print("Conectado:", versao[0])
            # Listar tabelas do schema
            tabelas = conn.execute(text("""
                SELECT tablename 
                FROM pg_tables 
                WHERE schemaname = CURRENT_SCHEMA();
            """)).fetchall()
            print(f"Tabelas no schema {schema}")
            for t in tabelas:
                print("-", t[0])
    except Exception as e:
        print("Erro:", e)
