import urllib.request, urllib.parse
import json

serviapi = ('https://pokeapi.co/api/v2/pokemon/')
var = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

while True:
    pokename = input('Enter pokemon name >>>').strip().lower()
    if not pokename: break
    url = serviapi + pokename
    print(url)
    request = urllib.request.Request(url, headers=var)
    urlopen = urllib.request.urlopen(request)
    data= urlopen.read().decode()
    pokemon_info = json.loads(data)
    
    print("Abilities:")
    for ability in pokemon_info['abilities']: print(ability['ability']['name'])
    