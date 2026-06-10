from supabase import Client

def salvar_no_supabase(supabase: Client, dados_tratados: dict):
    """Salva os dados tratados no Supabase."""
    print("Salvando lead no Supabase...")
    try:
        data, count = supabase.table("leads_diagnostico").insert(dados_tratados).execute()
        print(f"Sucesso! Lead {dados_tratados['nome']} salvo no banco de dados.")
    except Exception as e:
         print(f"Erro ao salvar no banco: {e}")