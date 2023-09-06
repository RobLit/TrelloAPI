import requests
import keys.trello
import json

def get():

    with open(keys.trello.path, "r") as file:
        board_id = file.read()
    url = f"https://api.trello.com/1/boards/{board_id}"

    response = requests.get(url, headers=keys.trello.headers, params=keys.trello.data)
    assert response.status_code == 200
    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

get()