import json
data = '''
[
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
]
'''
infodata = json.loads(data)
print('Brand count', len(infodata))

for item in infodata:
    print('Brand', item['brand'])
    print('Fuel', item['fuel']['value'])
    print('Max Speed',  item['max-speed'])