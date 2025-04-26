import json

ARQUIVO = "estoque.json"

def carregar_estoque():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_estoque(estoque):
    with open(ARQUIVO, "w") as f:
        json.dump(estoque, f, indent=4)

def adicionar_produto(nome, quantidade, preco):
    estoque = carregar_estoque()
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    salvar_estoque(estoque)

def exibir_estoque():
    estoque = carregar_estoque()
    total = 0
    for produto in estoque:
        print(f"{produto['nome']} - Quantidade: {produto['quantidade']} - Preço: {produto['preco']}")
        total += produto['quantidade'] * produto['preco']
    print(f"Valor total do estoque: R$ {total:.2f}")

