import os
import re
from supabase import create_client, Client
from dotenv import load_dotenv

def main() -> None:
    # --- 1. CONFIGURAÇÕES ---
    load_dotenv()
    SUPABASE_URL: str|None = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str|None = os.getenv("SUPABASE_KEY")

    # Instancia o cliente do Supabase
    supabase: Client = create_client(str(SUPABASE_URL), str(SUPABASE_KEY))

    # --- 2. O JSON SIMULADO ---
    # Simulando o payload que chega de um webhook
    payload_simulado = {
        "nome": "Dr. João Silva",
        "telefone": "+55 11 98765-4321", # Dado "sujo" (com espaços e traço)
        "email": "  contato@drjoao.com.br ", # Dado "sujo" (com espaços)
        "especialidade": "Cardiologia",
        "principal_desafio": "Falta de tempo para gerir Instagram"
    }


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro ao executar o script: {e}")