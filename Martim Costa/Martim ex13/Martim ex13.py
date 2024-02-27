import json
data = '''
{                     
"game_1":{             
    "name": "Warframe",
        "inf":{
            "tipo": "Looter Shooter, RPG",
            "hours played": "2.410h"
            }
        },
"game_2":{       
    "name": "Counter-stike",
        "inf":{
            "tipo":"First Person Shooter, competitive Shooter",
            "hours played":"1.363h"
            }
        },
"game_3":{
    "name": "Dauntless",
        "inf":{
            "tipo:":"Action RPG, CO-OP",
            "hours played":"743h"
        }
}
}
'''
info = json.loads(data)
print('Name:',info["game_3"]["name"])
print('Tipo', info["game_3"]["inf"])
