import re


def tratar_dados(lead: dict) -> dict:
    """Trata e normaliza os dados do lead recebido do webhook."""
    print("Iniciando tratamento de dados...")

    # 1. Normalizar E-mail (remover espaços e deixar minúsculo)
    email_limpo = lead.get("email", "").strip().lower()

    # 2. Formatar Telefone (remover tudo que não for número)
    telefone_limpo = re.sub(r"\D", "", lead.get("telefone", ""))

    # 3. Validação Básica
    if not lead.get("nome") or not email_limpo:
        raise ValueError("Erro: Nome e E-mail são obrigatórios!")

    return {
        "nome": lead.get("nome"),
        "telefone": telefone_limpo,
        "email": email_limpo,
        "especialidade": lead.get("especialidade"),
        "desafio": lead.get("principal_desafio"),
    }
