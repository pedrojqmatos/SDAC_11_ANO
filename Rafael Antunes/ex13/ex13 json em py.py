import json
data = '''

{
    "alimentos": [
      {
        "nome": "Maçã",
        "tipo": "Fruta",
        "cor": "Vermelho",
        "calorias": 52,
        "proteínas": 0.3,
        "gorduras": 0.2,
        "carboidratos": 14,
        "fibra": 2.4
      },
      {
        "nome": "Arroz",
        "tipo": "Grão",
        "cor": "Branco",
        "calorias": 130,
        "proteínas": 2.7,
        "gorduras": 0.3,
        "carboidratos": 28,
        "fibra": 0.6
      },
      {
        "nome": "Peito de Frango",
        "tipo": "Carne",
        "cor": "Branco",
        "calorias": 165,
        "proteínas": 31,
        "gorduras": 3.6,
        "carboidratos": 0,
        "fibra": 0
      },
      {
        "nome": "Picanha de Vaca",
        "tipo": "Carne",
        "cor": "Branco",
        "calorias": 450,
        "proteínas": 20,
        "gorduras": 35,
        "carboidratos": 0,
        "fibra": 0
      },
      {
        "nome": "Lombo de Carneiro",
        "tipo": "Carne",
        "cor": "Branco",
        "calorias": 300,
        "proteínas": 20,
        "gorduras": 25,
        "carboidratos": 0,
        "fibra":0
      }  
    ]
  }
'''

dados= json.loads(data)

for alimento in dados['alimentos']:
    print("Nome:", alimento['nome'])
    print("Tipo:", alimento['tipo'])
    print("Cor:", alimento['cor'])
    print("Calorias:", alimento['calorias'])
    print("Proteínas:", alimento['proteínas'])
    print("Gorduras:", alimento['gorduras'])
    print("Carboidratos:", alimento['carboidratos'])
    print("Fibra:", alimento['fibra'])
    print() 