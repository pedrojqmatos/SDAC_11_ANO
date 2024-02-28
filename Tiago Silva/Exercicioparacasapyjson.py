import json
data = '''[
  {
    "titulo" : "Homem-Aranha",
    "genero": {
      "type": "string",
      "value": "Super-Heróis"
    }
  },

  {
    "titulo" : "Forrest Gump",
    "genero": {
      "type": "string",
      "value": "Drama"
    }
  },

  {
    "titulo" : "Forrest Gump",
    "genero": {
      "type": "string",
      "value": "Drama"
      }
      "ano de lançamento:"{
      "type:" "integrer"
      "value" : 2001  
    }
  },

  {
    "titulo" : "Interstrelar",
    "genero": {
      "type": "string",
      "value": "Fição Científica"
    }
  }
]'''
info = json.loads(data)
for i in info :  
  print('titulo', i["titulo"])
  print('genero', i["genero"]["value"])
