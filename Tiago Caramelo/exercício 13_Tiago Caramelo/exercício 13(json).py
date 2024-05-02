import json

data ='''
   [
{
  "brandname" : "Calvin Klein",
  "id" :{
    "type": "int",
    "value" : "001"
  },
  "size" : {
    "type": "string",
    "value" : "XS"
  },
  "country" : {
    "type" : "string",
    "value" : "United States"
  },
  "colour" : {
    "type" : "string",
    "value" : "black"
  },
  "bottomwear" : {
    "type" : "string",
    "value": "jeans"
  },
  "footwear" : {
    "type" : "string",
    "value": "shoes"
  },
  "underwear" : {
    "type" : "string",
    "value": "boxers"
  }
},

{
  "brandname" : "Tommy Hilfiger",
  "id" :{
    "type": "int",
    "value" : "002"
  },
  "size" : {
    "type": "string",
    "value" : "S"
  },
  "country" : {
    "type" : "string",
    "value" : "United States"
  },
  "colour" : {
    "type" : "string",
    "value" : "blue"
  },
  "bottomwear" : {
    "type" : "string",
    "value": "jeans"
  },
  "footwear" : {
    "type" : "string",
    "value": "shoes"
  },
  "underwear" : {
    "type" : "string",
    "value": "boxers"
  }
},
{
  "brandname" : "Pepe Jeans",
  "id" :{
    "type": "int",
    "value" : "003"
  },
  "size" : {
    "type": "string",
    "value" : "M"
  },
  "country" : {
    "type" : "string",
    "value" : "United States"
  },
  "colour" : {
    "type" : "string",
    "value" : "red"
  },
  "bottomwear" : {
    "type" : "string",
    "value": "jeans"
  },
  "footwear" : {
    "type" : "string",
    "value": "shoes"
  },
  "underwear" : {
    "type" : "string",
    "value": "boxers"
  }
},
{
  "brandname" : "Gant",
  "id" :{
    "type": "int",
    "value" : "004"
  },
  "size" : {
    "type": "string",
    "value" : "L"
  },
  "country" : {
    "type" : "string",
    "value" : "United States"
  },
  "colour" : {
    "type" : "string",
    "value" : "white"
  },
  "bottomwear" : {
    "type" : "string",
    "value": "jeans"
  },
  "footwear" : {
    "type" : "string",
    "value": "shoes"
  },
  "underwear" : {
    "type" : "string",
    "value": "boxers"
  }
},
{
  "brandname" : "Lacoste",
  "id" :{
    "type": "int",
    "value" : "005"
  },
  "size" : {
    "type": "string",
    "value" : "XL"
  },
  "country" : {
    "type" : "string",
    "value" : "France"
  },
  "colour" : {
    "type" : "string",
    "value" : "green"
  },
  "bottomwear" : {
    "type" : "string",
    "value": "jeans"
  },
  "footwear" : {
    "type" : "string",
    "value": "shoes"
  },
  "underwear" : {
    "type" : "string",
    "value": "boxers"
  }
},
{
  "brandname" : "Nike",
  "id" :{
    "type": "int",
    "value" : "006"
  },
  "size" : {
    "type": "string",
    "value" : "XXL"
  },
  "country" : {
    "type" : "string",
    "value" : "United States"
  },
  "colour" : {
    "type" : "string",
    "value" : "pink"
  },
  "bottomwear" : {
    "type" : "string",
    "value": "jeans"
  },
  "footwear" : {
    "type" : "string",
    "value": "shoes"
  },
  "underwear" : {
    "type" : "string",
    "value": "boxers"
  }
},
{
  "brandname" : "Polo Ralph Lauren",
  "id" :{
    "type": "int",
    "value" : "007"
  },
  "size" : {
    "type": "string",
    "value" : "XXXL"
  },
  "country" : {
    "type" : "string",
    "value" : "United States"
  },
  "colour" : {
    "type" : "string",
    "value" : "purple"
  },
  "bottomwear" : {
    "type" : "string",
    "value": "jeans"
  },
  "footwear" : {
    "type" : "string",
    "value": "shoes"
  },
  "underwear" : {
    "type" : "string",
    "value": "boxers"
  }
}
]'''

Brands_data = json.loads(data)
print('Brand count', len(Brands_data))

for item in Brands_data:
    print('Brand Name: ', item['brandname'])
    print('Country: ', item['country']['value'])
    print('Size: ', item['size']['value'])
    print('Colour: ',  item['colour']['value'])
