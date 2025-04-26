import json

ARQUIVO = "reservas.json"

def inicializar_mapa(assentos=10):
    try:
        with open(ARQUIVO, "r") as f:
            json.load(f)
    except FileNotFoundError:
        mapa = ["Livre" for _ in range(assentos)]
        with open(ARQUIVO, "w") as f:
            json.dump(mapa, f, indent=4)

def carregar_mapa():
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar_mapa(mapa):
    with open(ARQUIVO, "w") as f:
        json.dump(mapa, f, indent=4)

def visualizar_mapa():
    mapa = carregar_mapa()
    for i, status in enumerate(mapa):
        print(f"Assento {i+1}: {status}")

def reservar_assento(numero):
    mapa = carregar_mapa()
    if mapa[numero-1] == "Livre":
        mapa[numero-1] = "Reservado"
        salvar_mapa(mapa)
    else:
        print("Assento já reservado!")

def cancelar_reserva(numero):
    mapa = carregar_mapa()
    if mapa[numero-1] == "Reservado":
        mapa[numero-1] = "Livre"
        salvar_mapa(mapa)
    else:
        print("Assento não está reservado!")

