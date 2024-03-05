import json
data = '''[ 
    { 
        "titulo": "The Legend of Zelda: Breath of the Wild", 
        "genero": "Ação/Aventura", 
        "plataforma": "Nintendo Switch", 
        "preco": "$59.99" 
    }, 
    { 
        "titulo": "Red Dead Redemption 2", 
        "genero": "Ação/Aventura", 
        "plataforma": "PlayStation 4", 
        "preco": "$39.99" 
    }, 
    { 
        "titulo": "Fortnite", 
        "genero": "Battle Royale", 
        "plataforma": "Multiplataforma", 
        "preco": "Grátis" 
    }, 
    { 
        "titulo": "FIFA 20", 
        "genero": "Esportes", 
        "plataforma": "Xbox One", 
        "preco": "$29.99" 
    }, 
    { 
        "titulo": "Minecraft", 
        "genero": "Sandbox", 
        "plataforma": "PC", 
        "preco": "$26.95" 
    }, 
    { 
        "titulo": "Call of Duty: Warzone",
        "genero": "Battle Royale", 
        "plataforma": "Multiplataforma", 
        "preco": "Grátis" 
    } 
]'''

jogos = json.loads(data)
print('Contagem de Jogos:', len(jogos))

for jogo in jogos: 
    print("Título:", jogo['titulo']) 
    print("Gênero:", jogo['genero']) 
    print("Plataforma:", jogo['plataforma']) 
    print("Preço:", jogo['preco'], '\n')