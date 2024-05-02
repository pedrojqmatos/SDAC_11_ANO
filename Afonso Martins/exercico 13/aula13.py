import json

data = [
    {
        "roupa": "sweat",
        "nome": "Camisola Nike Club",
        "tamanho": {
            "type": "int",
            "value": "xl"
        },
        "cor": {
            "type": "string",
            "value": "grey"
        },
        "preco": {
            "type": "float",
            "value": "44.00"
        }
    },
    {
        "roupa": "meias nike",
        "nome": "meias nike",
        "tamanho": {
            "type": "int",
            "value": "37-40"
        },
        "cor": {
            "type": "string",
            "value": "green"
        },
        "preco": {
            "type": "float",
            "value": "15.00"
        }
    },
    {
        "roupa": "calças",
        "nome": "The North Face Exploration Tapered",
        "tamanho": {
            "type": "int",
            "value": "xl"
        },
        "cor": {
            "type": "string",
            "value": "preto"
        },
        "preco": {
            "type": "float",
            "value": "85.00"
        }
    }
]

for item in data:
    print("Roupa:", item["roupa"])
    print("Nome:", item["nome"])
    print("Tamanho:", item["tamanho"]["value"])
    print("Cor:", item["cor"]["value"])
    print("Preço:", item["preco"]["value"])
    print("\n")
