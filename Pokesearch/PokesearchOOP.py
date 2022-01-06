import requests
from requests.models import Response

api_url = 'https://pokeapi.co/api/v2/'

class Pokemon:
    def __init__(self, name, api_url):
        self.name = name
        self.url = (api_url + 'pokemon' + '/' + name)
        self.api_url = api_url

    def Search(name, api_url):
        pokeurl = (api_url + 'pokemon' + '/' + name)
        response = requests.get(pokeurl)
        print('connection status:', response.status_code)
        if response.status_code == 200:
            print('Connected!')
            print('Pokemon found...')
            print('Name:', response.json()['name'].title())
            print('Pokedex ID:', response.json()['id'])
        if response.status_code == 404:
            print('Pokemon not found')
            return
        
        else:
            print('Not Connected! Try again!')

    def Types(name, api_url):
        pokeurl = (api_url + 'pokemon' + '/' + name)
        response = requests.get(pokeurl)
        types = response.json()['types']
        loop1 = 0
        while loop1 < 2:
            print('Type',loop1 + 1, ':', response.json()['types'][loop1]['type']['name'])
            loop1 = loop1 + 1

        print('Weight:', response.json()['weight'])

    def Moves(api_url, name):
        loop = 0
        pokeurl = (api_url + 'pokemon' + '/' + name)
        response = requests.get(pokeurl)
        search_moves = response.json()['moves']
        lensearch = len(search_moves)
        print(lensearch, ' moves found!')

        for lensearch in search_moves:    
            print('move',loop + 1,':\t', response.json()['moves'][loop]['move']['name'])
            loop = loop + 1
    
    def Stats(api_url, name):
        pokeurl = (api_url + 'pokemon' + '/' + name)
        response = requests.get(pokeurl)
        print('stat:\t', response.json()['stats'][0]['stat']['name'])
        print('value:\t', response.json()['stats'][0]['base_stat'])
        print()
        print('stat:\t', response.json()['stats'][1]['stat']['name'])
        print('value:\t', response.json()['stats'][1]['base_stat'])
        print()
        print('stat:\t', response.json()['stats'][2]['stat']['name'])
        print('value:\t', response.json()['stats'][2]['base_stat'])
        print()
        print('stat:\t', response.json()['stats'][3]['stat']['name'])
        print('value:\t', response.json()['stats'][3]['base_stat'])
        print()
        print('stat:\t', response.json()['stats'][4]['stat']['name'])
        print('value:\t', response.json()['stats'][4]['base_stat'])
        print()
        print('stat:\t', response.json()['stats'][5]['stat']['name'])
        print('value:\t', response.json()['stats'][5]['base_stat'])        


def main():
    loop = 0
    name = input('search a pokemon, or input pokedex id: ')
    Pokemon.Search(name, api_url)
    Pokemon.Types(name, api_url)
    while loop == 0:
        search = input('search poke data (moves or stats), or exit to exit: ')
        
        if search == 'exit':
            break
        
        if 'stats' in search:
            Pokemon.Stats(name, api_url)

        if 'moves' in search:
            Pokemon.Moves(name, api_url)

main()

#if __name__ == "__main__":
    #main()