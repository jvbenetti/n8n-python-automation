# 🚀 Pipeline de Automação: Gestão de Conteúdo e Leads

Este projeto é uma Prova de Conceito (PoC) arquitetural dividida em duas frentes integradas: uma orquestração visual de fluxos de trabalho (usando **n8n**) e um processamento de dados via backend (usando **Python**). O objetivo central é eliminar tarefas repetitivas, unificando a gestão de conteúdo de redes sociais e o tratamento de leads em uma infraestrutura única baseada em PostgreSQL (Supabase) e ClickUp.

---

## 🏗️ Arquitetura do Projeto

O repositório está dividido em dois módulos independentes, mas que compartilham a mesma lógica de infraestrutura (Supabase) para persistência de dados.

### 1. Módulo n8n (Orquestração e IA)
Localizado na pasta `/n8n`. Responsável por automatizar aprovações de conteúdo.

* **O Fluxo:** Recebe um payload de uma tarefa aprovada, envia para um modelo de Inteligência Artificial sugerir hashtags, salva os dados no banco e notifica a equipe no Telegram.
* **Decisões Técnicas:**
    * **Event-Driven (Webhooks) vs Polling:** Optei por usar Webhooks para engatilhar a automação. Isso economiza requisições desnecessárias ao servidor em comparação ao *polling* constante (checagem a cada X minutos) e permite respostas em tempo real.
    * **Sanitização de IA:** IAs generativas frequentemente injetam blocos de markdown (` ```json `) nas respostas. Implementei uma camada de limpeza via Regex diretamente nas expressões do n8n antes do `JSON.parse` para garantir que o fluxo não quebre caso a IA fuja do formato estrito.
    * **Ambiente Docker:** O ambiente local utiliza a variável `N8N_SECURE_COOKIE=false` no docker-compose para permitir o tráfego HTTP no localhost sem bloqueio de segurança dos navegadores. Em um ambiente produtivo, isso rodaria atrás de um proxy reverso com HTTPS.

### 2. Módulo Python (Tratamento de Dados de Leads)
Localizado na pasta `/python`. Um script backend focado em receber dados "sujos" de um formulário de diagnóstico, tratá-los e orquestrar APIs.

* **O Fluxo:** Recebe o payload do lead, normaliza e-mails (trim/lower), formata números de telefone usando expressões regulares para manter apenas dígitos, insere no banco PostgreSQL e formata o payload para a API de criação de tarefas.
* **Decisões Técnicas:**
    * **Modularização:** Separação clara de responsabilidades (limpeza em `cleaner.py` e persistência em `db.py`) utilizando `python-dotenv` para segurança de credenciais.
    * **Supabase como Single Source of Truth:** Tanto o n8n quanto o script Python apontam para o mesmo banco, demonstrando coesão na stack tecnológica. O campo de chave primária (`id`) foi delegado ao banco usando propriedade `Identity`, prevenindo conflitos de concorrência nas requisições.

---

## 📈 Próximos Passos (Visão de Melhorias)

Caso este sistema fosse escalado para um ambiente de produção com alto volume, algumas implementações adicionais seriam essenciais:

1.  **Error Handling Global (n8n):** Criação de um *Error Trigger Workflow* secundário no n8n. Se a API de IA ou o banco ficassem indisponíveis, o fluxo principal falharia graciosamente e dispararia um alerta técnico no Slack/Telegram.
2.  **Tratamento de Rate Limits:** Em cenários de picos de acessos, a API do Telegram e do banco podem sofrer *throttling*. Seria ideal implementar nós de "Wait" dinâmicos no n8n ou uma fila assíncrona (RabbitMQ/Celery) no backend Python.
3.  **Tipagem Estrita e Testes (Python):** Adição do `pydantic` para validação rigorosa dos payloads de entrada, além de testes unitários com `pytest` para a camada de sanitização de strings.

---

## 💻 Como executar o projeto

**Subindo a Orquestração (n8n):**
1. Na raiz do projeto, execute: `docker-compose up -d`
2. Importe o arquivo `workflow.json` (dentro da pasta `/n8n`) na interface do n8n.

**Executando o Backend (Python):**
1. Entre na pasta: `cd python`
2. Crie e ative um ambiente virtual: `python -m venv venv` e `source venv/bin/activate`
3. Instale as dependências: `pip install -r requirements.txt`
4. Crie um arquivo `.env` com suas credenciais do Supabase.
5. Execute o script: `python main.py`