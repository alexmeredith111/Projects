import requests

url = "https://api.spacexdata.com/v3/"
response = requests.get(url)
status_code = response.status_code

def api_addon():
    print('''
    Search SpaceX parts and missions:
    [1] Capsules
    [2] Cores
    [3] Dragons
    [4] History
    [5] Info
    [6] Landing Pads    
    [7] Launches
    [8] Launch Pads
    [9] Missions
    [10] Payloads
    [11] Rockets
    [12] Roadster
    [13] Ships
    ''')
    search_queary = input('> ')
    if search_queary == '1':
        capsules_url = url + 'capsules'
        capsule_response = requests.get(capsules_url)
        capsule_search_input = input('search capsules from 1-18: ')
        if capsule_search_input == '1' in capsule_search_input[0]:
            prompt = int(capsule_search_input) - 1

        print('serial: ',capsule_response.json()[prompt]['capsule_serial'])
        print('id: ',capsule_response.json()[prompt]['capsule_id'])
        print('status: ',capsule_response.json()[prompt]['status'])
        print('original launch: ',capsule_response.json()[prompt]['original_launch'])
        print('landings: ',capsule_response.json()[prompt]['landings'])
        print('type: ',capsule_response.json()[prompt]['type'])
        print('details: ',capsule_response.json()[prompt]['details'])
        print('reuse count: ',capsule_response.json()[prompt]['reuse_count'])

    if search_queary == '2':
        cores_url = url + 'cores'
        cores_response = requests.get(cores_url)
        cores_search_input = input('search ccores from 1-63: ')
        if cores_search_input == '1' in cores_search_input[0]:
            prompt = int(cores_search_input) - 1

        print('serial: ',cores_response.json()[prompt]['core_serial'])
        print('status: ',cores_response.json()[prompt]['status'])
        print('original launch: ',cores_response.json()[prompt]['original_launch'])
        print('landings: ',cores_response.json()[prompt]['rtls_landings'])
        print('water landing: ',cores_response.json()[prompt]['water_landing'])
        print('details: ',cores_response.json()[prompt]['details'])
        print('reuse count: ',cores_response.json()[prompt]['reuse_count'])  

    if search_queary == '3':
        dragons_url = url + 'dragons'
        dragons_response = requests.get(dragons_url)
        dragons_search_input = input('search dragons from 1-2: ')
        if dragons_search_input == '1' in dragons_search_input[0]:
            prompt = int(dragons_search_input) - 1

        print('serial: ',dragons_response.json()[prompt]['name'])
        print('id: ',dragons_response.json()[prompt]['type'])
        print('active: ',dragons_response.json()[prompt]['active'])
        print('original launch: ',dragons_response.json()[prompt]['first_flight'])
        print('dry mass kg : ',dragons_response.json()[prompt]['dry_mass_kg'])
        print('orbit time: ',dragons_response.json()[prompt]['orbit_duration_yr'], 'years')
        print('crew capacity: ',dragons_response.json()[prompt]['crew_capacity'])
    




    #if search_queary == 4
    #if search_queary == 5
    #if search_queary == 6
    #if search_queary == 7
    #if search_queary == 8
    #if search_queary == 9
    #if search_queary == 10
    #if search_queary == 11
    #if search_queary == 12
    #if search_queary == 13


def connection_status():
    print(status_code)
    if status_code == 200:
        print('Connected!')
    
    else:
        print('Not Connected!')


def main():
    connection_status()
    api_addon()

main()