import json
data = '''[
{
    "game": "Valorant",
    "genre": {
        "type" : "string",
        "value": "First Person Shooter, competitive Shooter"
    },
    "hours-played": "743h"
}, 
    
{
    "game": "Valorant",
    "genre": {
        "type" : "string",
        "value": "First Person Shooter, competitive Shooter"
    },
    "hours-played": "743h"
}, 

{
"game": "Valorant",
"genre": {
    "type" : "string",
    "value": "First Person Shooter, competitive Shooter"
},
"hours-played": "743h"
}, 

{
    "game": "Valorant",
    "genre": {
        "type" : "string",
        "value": "First Person Shooter, competitive Shooter"
    },
    "hours-played": "743h"
}
]
'''
info = json.loads(data)

for item in info:
    print('Game:',item["game"])
    print('Genre:', item["genre"]["value"])
    print('Hours Played:', item["hours-played"])