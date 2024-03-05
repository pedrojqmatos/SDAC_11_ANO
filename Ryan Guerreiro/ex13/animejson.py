import json
code = """[
{
    "anime" : "Demon Slayer",
    "original name" : "Kimetsu no Yaiba (鬼滅きめつの刃)",
    "creation": {
        "type": "string",
        "year": "2019",
        "creator": "Koyoharu Gotouge"
},
    "main character": "Tanjiro Kamado",
    "volumes": "23",
    "episodes": "26",
    "state": "finished"
} ,

{
    "anime" : "Sorcerer Battle",
    "original name" : "Jujutsu Kaisen (呪術廻戦)",
    "creation": {
        "type": "string",
        "year": "2017",
        "creator": "Gege Akutami"
},
    "main character": "Yuji Itadori",
    "volumes": "25",
    "episodes": "47",
    "state": "in progress"
} ,

{
    "anime" : "Attack on Titan",
    "original name" : "Shingeki no Kyojin (進撃の巨人)",
    "creation": {
        "type": "string",
        "year": "2009",
        "creator": "Hajime Isayama"
},
    "main character": "Eren Yeager",
    "volumes": "34",
    "episodes": "88",
    "state": "finished"
} ,

{
    "anime" : "Berserk",
    "original name" : "Berserk (ベルセルク)",
    "creation": {
        "type": "string",
        "year": "1989",
        "creator": "Kentaro Miura"
},
    "main character": "Guts",
    "volumes": "42",
    "episodes": "25",
    "state": "in progress"
} 
]"""

JSON = json.loads(code) 

#ira contar quantas vezes aparece os animes
print('Anime counter:', len(JSON), '\n')


#informação que será fornecida
for anime in JSON: 
    print("Anime:", anime["anime"]) ; print("Original name:", anime["original name"]) ; 
    print("Created by:", anime["creation"]["creator"]) ; 
    print("Main character", anime["main character"]) ; print("Volumes:", anime["volumes"]) ; 
    print("Episodes", anime["episodes"]) ; print("State:", anime["state"]) 
    print()
