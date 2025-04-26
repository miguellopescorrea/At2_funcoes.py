import json
from datetime import datetime

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa(descricao, prazo):
    tarefas = carregar_tarefas()
    tarefas.append({"descricao": descricao, "prazo": prazo, "concluida": False})
    salvar_tarefas(tarefas)

def listar_tarefas():
    tarefas = carregar_tarefas()
    tarefas.sort(key=lambda x: datetime.strptime(x["prazo"], "%Y-%m-%d"))
    for i, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i+1}. {tarefa['descricao']} - Prazo: {tarefa['prazo']} - {status}")

def concluir_tarefa(indice):
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)

# Exemplo de uso:
# adicionar_tarefa("Entregar trabalho", "2025-04-30")
# listar_tarefas()
# concluir_tarefa(0)
# listar_tarefas()
