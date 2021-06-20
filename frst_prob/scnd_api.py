import requests

API_KEY = 'AIzaSyA5bwbEsAOUMOI4RK2zXcIayG4vjuQSpcw'


def addr_coordinate(address):
    params = {
    'key': API_KEY,
    'address': address }
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params).json()
    response.keys()

    if response['status'] == 'OK':
        geometry = response['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']
        crdnt = []
        crdnt.append(lat)
        crdnt.append(lon)
        print("done")
    return crdnt

print("done")
