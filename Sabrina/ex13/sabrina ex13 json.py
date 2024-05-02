import json
data = ''' {
    "restaurante1":{
        "name": "Burguer King",
        "local": "santarem",
        "tipo de comida":"Fast Food "
    },
    "restaurante2":{
        "name":"La Bella",
        "local":"santarem",
        "tipo de comida":"Comida Italiana"
    },
    "restaurante3":{
        "name":"EL Mexicano",
        "local":"santarem",
        "tipo de comida":"Comida Mexicana"
    }
}'''
info = json.loads(data)

print('Name:',info["restaurante1"]['name'])
print("local:",info["restaurante1"]["local"])
print("tipo de comida:",info["restaurante1"]["tipo de comida"])
print('Name:',info["restaurante2"]['name'])
print("local:",info["restaurante2"]["local"])
print("tipo de comida:",info["restaurante2"]["tipo de comida"])
print('Name:',info["restaurante3"]['name'])
print("local:",info["restaurante3"]["local"])
print("tipo de comida:",info["restaurante3"]["tipo de comida"])

