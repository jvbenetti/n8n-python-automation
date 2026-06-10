import json


def criar_tarefa_clickup_simulada(dados_tratados: dict):
    """Simula a criação de uma tarefa no ClickUp usando os dados tratados do lead."""
    print("\nPreparando criação de tarefa no ClickUp (Simulação)...")

    # URL fictícia da API do ClickUp
    url_clickup = "https://api.clickup.com/api/v2/list/12345678/task"

    # Headers obrigatórios para APIs REST
    headers = {
        "Authorization": "Bearer CHAVE_DE_API_CLICKUP",
        "Content-Type": "application/json",
    }

    # Montagem do Payload (Corpo da requisição) no formato que o ClickUp exige
    payload_clickup = {
        "name": f"Novo Lead (Diagnóstico): {dados_tratados['nome']}",
        "description": f"Contato: {dados_tratados['telefone']} | Email: {dados_tratados['email']}\nEspecialidade: {dados_tratados['especialidade']}\nDesafio: {dados_tratados['desafio']}",
        "status": "TO DO",
        "priority": 3,
        "assignees": [12345],  # ID simulado de um responsável
    }

    # SIMULAÇÃO DO ENVIO:
    # Se fôssemos rodar de verdade, faríamos:
    # response = requests.post(url_clickup, headers=headers, json=payload_clickup)
    # if response.status_code == 200:
    #    print("Tarefa criada com sucesso!")

    print("\n--- PAYLOAD MONTADO PARA A API DO CLICKUP ---")
    print(json.dumps(payload_clickup, indent=4, ensure_ascii=False))
    print("---------------------------------------------")
