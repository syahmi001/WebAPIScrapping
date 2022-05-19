import requests


def get_json(url):
    r = requests.get(url)
    json_data = r.json()
    return json_data
