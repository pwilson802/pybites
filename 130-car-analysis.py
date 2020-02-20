from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    return Counter([(x['automaker'], x['year']) for x in data if x['year'] == year]).most_common()[0][0][0]


def get_models(automaker, year):
    return {x['model'] for x in data if (x['automaker'] == automaker) and (x['year'] == year)}