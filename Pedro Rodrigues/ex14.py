#ex14

import urllib.request, urllib.parse
import http, json, ssl

service_url = 'https://pokeapi.co'

while True:
    poke_name = input('Enter location: ')
    if len(poke_name) < 1: 
        break
    