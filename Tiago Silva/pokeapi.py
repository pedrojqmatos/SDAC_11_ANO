import urllib.request, urllib.parse, urllib.error
import json

site = 'https://pokeapi.co/api/v2/pokemon/'

while True :
    pokemon = input("Escolhe o pokemon (ou pressiona Enter para sair):").strip()
    if not pokemon :
        break

    url = site + pokemon.lower() 
    print('A devolver', url)

#Define o user agent para imitar o browser da web

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like GECKO) Chrome/58.0.3029.110 Safari/537.3'}
    try :
        request = urllib.request.Request(url, headers=headers)
        uh = urllib.request.urlopen(request)
        data = uh.read().decode()
    except urllib.error.HTTPError as w :
        if w.code == 404:
           print(f'{pokemon} O pokemon não foi encontrado na pokedex')
        else :
           print(f'HTTP Error: {w.code} para {pokemon}' ) 
        continue

    js  = json.loads(data)

    name = js.get('name')
    abilities = [ability['ability']['name'] for ability in js.get('abilities', [])]
    base_experience = js.get('base_experience')
    moves = [move['move']['name'] for move in js.get('moves',[])]

    print(f"Name: {name}, Abilities: {', '.join(abilities)}, Base Experience: {base_experience}, Moves: {', '.join(moves)}")





