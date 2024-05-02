import json

code='''[
    {
        "name": "nikeSB",
        "style": "Skate shoes",
        "sizenumber": "43",
        "color": "yelow/gren",
        "orders": "41",
        "price": "450€",
        "material": "canvas"
    },
    {
        "name": "nike air max 97",
        "style": "training shoes",
        "sizenumber": "34",
        "color": "black/wite",
        "orders": "13",
        "price": "250€",
        "material": "mesh"
    },
    {
        "name": "new balance",
        "style": "all in 1",
        "sizenumber": "46",
        "color": "black/blue",
        "orders": "23",
        "price": "120€",
        "material": "canvas"
    },
    {
        "name": "nike",
        "style": "air max",
        "sizenumber": "42",
        "color": "black/red",
        "orders": "45",
        "price": "150€",
        "material": "leather"

    },
    {
        "name": "adidas superstar",
        "style": "classic",
        "sizenumber": "38",
        "color": "white/black",
        "orders": "55",
        "price": "120€",
        "material": "leather"
    },
    {
        "name": "converse chuck taylor",
        "style": "high top",
        "sizenumber": "40",
        "color": "red",
        "orders": "28",
        "price": "80€",
        "material": "canvas"
    },
    {
        "name": "nike react element",
        "style": "running shoes",
        "sizenumber": "41",
        "color": "blue/green",
        "orders": "37",
        "price": "160€",
        "material": "mesh"
    },
    {
        "name": "reebok classic",
        "style": "retro",
        "sizenumber": "43",
        "color": "white/navy",
        "orders": "20",
        "price": "100€",
        "material": "suede"
    }
]'''

SJASON = json.loads(code)
print ('name count: ',len(SJASON))

for shoes in SJASON: 
    print('Name: ', shoes["name"])
    print('Style: ', shoes["style"])
    print('Sizenumber: ', shoes["sizenumber"])
    print('Color: ', shoes["color"])
    print('Orders: ', shoes["orders"])
    print('Price: ', shoes["price"])
    print('Material: ', shoes["material"])