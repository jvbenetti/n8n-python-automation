import os
from dotenv import load_dotenv
from supabase import create_client, Client
from utils import tratar_dados, salvar_no_supabase, criar_tarefa_clickup_simulada


def main() -> None:
    # --- 1. CONFIGURAÇÕES ---
    load_dotenv()
    SUPABASE_URL: str | None = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str | None = os.getenv("SUPABASE_KEY")

    # Instancia o cliente do Supabase
    supabase: Client = create_client(str(SUPABASE_URL), str(SUPABASE_KEY))

    # --- 2. O JSON SIMULADO ---
    # Simulando o payload que chega de um webhook
    payload_simulado = {
        "nome": "Dr. João Silva",
        "telefone": "+55 11 98765-4321",  # Dado "sujo" (com espaços e traço)
        "email": "  contato@drjoao.com.br ",  # Dado "sujo" (com espaços)
        "especialidade": "Cardiologia",
        "principal_desafio": "Falta de tempo para gerir Instagram",
    }

    # --- 3. TRATAMENTO DOS DADOS ---
    dados_tratados = tratar_dados(payload_simulado)

    # --- 4. SALVAMENTO NO BANCO DE DADOS ---
    salvar_no_supabase(supabase, dados_tratados)

    # --- 5. SIMULAÇÃO DE CRIAÇÃO DE TAREFA NO CLICKUP ---
    criar_tarefa_clickup_simulada(dados_tratados)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro ao executar o script: {e}")
