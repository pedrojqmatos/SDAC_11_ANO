import json 
data = '''[
{
    "vestuario" : "calcas",
    "nome" : "Calças",
    "tamanho" : {
        "type": "int",
        "value": "32"
    },
    "cor" : {
        "type": "string",
        "value" : "Preto"
    },
    "preco" : {
        "type": "float",
        "value": "35.00"
    }
},

{
    "vestuario" : "Roupa",
    "nome" : "Camisas",
    "tamanho" : {
        "type": "int",
        "value": "M"
    },
    "cor" : {
        "type": "string",
        "value" : "azul"
    },
    "preco" : {
        "type": "float",
        "value": "20.00"
    }
},

{
    "vestuario" : "casaco",
    "nome" : "Casaco",
    "tamanho" : {
        "type": "int",
        "value": "xs"
    },
    "cor" : {
        "type": "string",
        "value" : "vermelho"
    },
    "preco" : {
        "type": "float",
        "value": "45.00"
    }
}
]'''
info = json.loads(data)
for item in info:
    print('nome', item ["nome"])
    print('nome', item ["tamanho"]["value"])
    print('nome', item ["preco"]["value"])
    