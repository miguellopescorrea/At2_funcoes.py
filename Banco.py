import json

ARQUIVO = "usuarios.json"

def carregar_usuarios():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as f:
        json.dump(usuarios, f, indent=4)

def criar_usuario(usuario, senha):
    usuarios = carregar_usuarios()
    usuarios[usuario] = {"senha": senha, "saldo": 0.0, "transacoes": []}
    salvar_usuarios(usuarios)

def login(usuario, senha):
    usuarios = carregar_usuarios()
    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        return True
    return False

def deposito(usuario, valor):
    usuarios = carregar_usuarios()
    usuarios[usuario]["saldo"] += valor
    usuarios[usuario]["transacoes"].append(f"Depósito de R$ {valor:.2f}")
    salvar_usuarios(usuarios)

def saque(usuario, valor):
    usuarios = carregar_usuarios()
    if usuarios[usuario]["saldo"] >= valor:
        usuarios[usuario]["saldo"] -= valor
        usuarios[usuario]["transacoes"].append(f"Saque de R$ {valor:.2f}")
        salvar_usuarios(usuarios)
    else:
        print("Saldo insuficiente!")

def extrato(usuario):
    usuarios = carregar_usuarios()
    print(f"Saldo atual: R$ {usuarios[usuario]['saldo']:.2f}")
    print("Transações:")
    for t in usuarios[usuario]["transacoes"]:
        print(t)
