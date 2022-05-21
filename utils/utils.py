import requests
import json
from datetime import datetime


def get_json(url):
    req = requests.get(url)
    data = json.loads(req.content)

    # Sort the data using date in descending order
    sorted_data = sorted(data['results'], key=lambda x: datetime.strptime(x['published_date'], '%Y-%m-%d'), reverse=True)
    return sorted_data
