import requests
from requests.models import Response
import json

api_url = 'https://pokeapi.co/api/v2/'
loop = 0


prompt2 = input('Search pokemon or pokedex ID: ')



pokeurl = (api_url + 'pokemon' + '/' + prompt2)
pokesponse = requests.get(pokeurl)
print('connection status:', pokesponse.status_code)

if pokesponse.status_code == 200:
    print('Pokemon found...')
    print('Name:', pokesponse.json()['name'].title())
    print('Pokedex ID:', pokesponse.json()['id'])
    
    searchsponse2 = pokesponse.json()['types']
    loop1 = 0
    for key in searchsponse2:
        print('Type:', pokesponse.json()['types'][loop1]['type']['name'])
        loop1 = loop1 + 1

    print('Weight:', pokesponse.json()['weight'])

while loop == 0:
    search = input('search poke data (moves or stats), or exit to exit: ')
        
    if search == 'exit':

        loop = loop + 1
        
    else:
        searchresults = (search,':', pokesponse.json()[search])

        if search == 'stats':
            print('stat:\t', pokesponse.json()['stats'][0]['stat']['name'])
            print('value:\t', pokesponse.json()['stats'][0]['base_stat'])
            print()
            print('stat:\t', pokesponse.json()['stats'][1]['stat']['name'])
            print('value:\t', pokesponse.json()['stats'][1]['base_stat'])
            print()
            print('stat:\t', pokesponse.json()['stats'][2]['stat']['name'])
            print('value:\t', pokesponse.json()['stats'][2]['base_stat'])
            print()
            print('stat:\t', pokesponse.json()['stats'][3]['stat']['name'])
            print('value:\t', pokesponse.json()['stats'][3]['base_stat'])
            print()
            print('stat:\t', pokesponse.json()['stats'][4]['stat']['name'])
            print('value:\t', pokesponse.json()['stats'][4]['base_stat'])
            print()
            print('stat:\t', pokesponse.json()['stats'][5]['stat']['name'])
            print('value:\t', pokesponse.json()['stats'][5]['base_stat'])

        if search == 'moves':
            search_moves = pokesponse.json()['moves']
            lensearch = len(search_moves)
            print(lensearch, ' moves found!')

            loop2 = 0
            
            for lensearch in search_moves:    
                print('move',loop2 + 1,':\t', pokesponse.json()['moves'][loop2]['move']['name'])
                loop2 = loop2 + 1
    

if pokesponse.status_code == 404:
    print('Pokemon not found')
