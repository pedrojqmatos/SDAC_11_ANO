import urllib.request, urllib.error, urllib.parse
import json

serviceurl = 'https://pokeapi.co/api/v2/pokemon/'
var = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

while True:
    pokename = input('Enter Pokemon: ').strip().lower()
    if not pokename:  
        break
    url = serviceurl + pokename

    try:
        resquestpoke = urllib.request.Request(url, headers=var)
        urlopen = urllib.request.urlopen(resquestpoke)
        data = urlopen.read().decode()
    except urllib.error.HTTPError as error : 
        if error.code == 404:
            print(f"{pokename} Pokémon not found on the pokedex.")
        else:
            print(f"HTTP error: {error.code} for {pokename}")
        continue
    
    info = json.loads(data)
    print("Abilities : ")
    if 'abilities' in info:
        for ability in info['abilities']:
            print(ability['ability']['name'])
    else:
        print("No abilities found for", pokename)
    
