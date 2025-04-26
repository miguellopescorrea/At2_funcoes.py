import json

ARQUIVO = "contatos.json"

def carregar_contatos():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_contatos(contatos):
    with open(ARQUIVO, "w") as f:
        json.dump(contatos, f, indent=4)

def adicionar_contato(nome, telefone, email):
    contatos = carregar_contatos()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvar_contatos(contatos)

def buscar_contato(nome):
    contatos = carregar_contatos()
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
            return
    print("Contato não encontrado!")

