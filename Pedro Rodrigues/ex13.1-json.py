#ex13.1-json

import json

data = '''[
    {
      "jogador" : "Cristiano Ronaldo",
      "modalidade": {
        "type": "string",
        "value": "Futebol"
      },
      "age": {
        "type": "float",
        "value": 38
      }
    },
  
    {
      "jogador" : "Lebron James",
      "modalidade": {
        "type": "string",
        "value": "Basquetebol"
      },
      "age": {
        "type": "float",
        "value": 35
      }
    },
  
    {
      "jogador" : "Carlos Alcaraz",
      "modalidade": {
        "type": "string",
        "value": "Ténis"
      },
      "age": {
        "type": "float",
        "value": 20
      }
    }
  ]'''

info = json.loads(data)

for item in info:
    print('Nome do jogador:', item["jogador"])
    print('Modalidade praticada: ', item["modalidade"]["value"])
    print('Idade do jogador: ', item["age"]["value"])