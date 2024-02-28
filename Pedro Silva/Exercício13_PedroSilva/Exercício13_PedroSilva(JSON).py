import json

code = '''[
{
    "brand" : "Toyota",
    "id" : "001",
    "model": "Corolla",
    "fuel": {
        "type": "string",
        "value": "Diesel"
},
    "max-speed": "178km/h",
    "weight": "1024kg",
    "doors": "5"
} ,

{
    "brand" : "Mercedes",
    "id" : "002",
    "model": "Benz",
    "fuel": {
        "type": "string",
        "value": "Petrol"
},
    "max-speed": "190km/h",
    "weight": "1045kg",
    "doors": "4"
},

{
    "brand" : "BMW",
    "id" : "003",
    "model": "i7",
    "fuel": {
        "type": "string",
        "value": "Diesel"
},
    "max-speed": "190km/h",
    "weight": "1045kg",
    "doors": "4"
}
]'''

JSON = json.loads(code) #guarda a biblioteca da "code"
print('User count:', len(JSON)) #ira contar quantas vezes aparece "brand"
#informação requerida
for car in JSON: print("Brand:", car["brand"]) ; print("Model:", car["model"]) ; print("Fuel:", car["fuel"]["value"])
