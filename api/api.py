import requests
import json
import os

async def getNPeople(location):
    params = {'Content-Type': 'application/json'}
    response = requests.get(f'https://visits.evofitness.no/api/v1/locations/{location}/current')
    return response