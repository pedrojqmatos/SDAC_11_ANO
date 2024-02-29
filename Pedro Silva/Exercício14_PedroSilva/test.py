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


    #bibli urlilb var e url
    urlopen = .request.urlopen(url)
    data= urlopen.read().decode()
    




while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    address = address.strip()
    parms = dict()
    parms['q'] = address
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    js = json.loads(data)
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']