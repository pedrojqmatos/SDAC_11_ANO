import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://pokeapi.co/api/v2/pokemon/'

while True:
    pokemon = input('Enter pokemon (or press Enter to quit): ').strip()
    if not pokemon:
        break
    
    url = serviceurl + pokemon.lower()
    print('Retrieving', url)

    #Define User Agent to mimic web browser
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try :
        req = urllib.request.Request(url, headers=headers)
        uh = urllib.request.urlopen(req)
        data = uh.read().decode()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"{pokemon} Pokemon not found on the pokedex")
        else:
            print(f"HTTP Error: {e.code} for {pokemon}")
        continue

    js = json.loads(data)

    # Extracted details for demonstration
    name = js.get('name')
    abilities = [ability['ability']['name'] for ability in js.get('abilities', [])]
    base_experience = js.get('base_experience')
    moves = [move['move']['name'] for move in js.get('moves',[])]

    print(f"Name: {name}, Abilities: {', '.join(abilities)}, Base Experience: {base_experience}, Moves: {', '.join(moves)}")