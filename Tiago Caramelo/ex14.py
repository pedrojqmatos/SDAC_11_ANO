import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://pokeapi.co/api/v2/pokemon/'

while True: 
    pokemon = input('Enter pokemon (or press Enter to quit): ').strip()
    if not pokemon:
        break

    url = serviceurl + pokemon.lower()
    print('Retrieving', url)

    #define User Agent to mimic web browser
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} 
    try :
        req = urllib.request.Request(url, headers=headers)
        uh = urllib.request.urlopen(req)
        data = uh.read().decode()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"{pokemon} Pokemon not found on the pokedex")
        else:
            print(f"HTTPError: {e.code} for {pokemon}")
        continue

    js = json.loads(data)

    #Estracted details for demonstration
    name = js.get('name')
    abilities = [ability['ability'] for ability in js.get]
