import urllib.request, urllib.parse
import json

serviapi = ('https://pokeapi.co/api/v2/pokemon/')
var = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

while True:
    pokename = input('Enter pokemon name >>>').strip()
    pokename = pokename.lower()
    if not pokename: break
    url = serviapi + pokename.lower()
    print(url)
    request = url.request
    