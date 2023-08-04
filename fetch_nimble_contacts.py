import requests


def fetch_nimble_contacts():
    """ Gets contact data from the Nimble service """
    url = "https://api.nimble.com/api/v1/contacts"
    headers = {"Authorization": "Bearer NxkA2RlXS3NiR8SKwRdDmroA992jgu"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
