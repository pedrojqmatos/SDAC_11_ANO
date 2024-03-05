import json
data = ''' {
    "restaurante1":{
        "name": "Burguer King",
        "local": "santarem",
        "tipo de comida":"Fast Food "
    },
    "restaurante_2":{
        "name":"La Bella",
        "local":"santarem",
        "tipo de comida":"Comida Italiana"
    },
    "restaurante_3":{
        "name":"EL Mexicano",
        "local":"santarem",
        "tipo de comida":"Comida Mexicana"
    }
}'''
info = json.loads(data)

print('Name:',info["restaurante1"]['name'])
