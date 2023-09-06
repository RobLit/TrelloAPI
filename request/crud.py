import requests
import keys.trello

def create():
    url = "https://api.trello.com/1/boards/"
    data = {
        'name': 'new_board'
    }
    response = requests.post(url, data=data, params=keys.trello.data)
    data = response.json()
    board_id = data['id']
    with open(keys.trello.path, "w") as file:
        file.write(board_id)
    assert response.status_code == 200
create()

def get_id_list2():
    with open(keys.trello.path, "r") as file:
        board_id = file.read()
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    response = requests.get(url, headers=keys.trello.headers, params=keys.trello.data)
    query = response.json()
    keys.trello.fst = query[0]['id']
    keys.trello.snd = query[1]['id']
    keys.trello.trd = query[2]['id']
get_id_list2()

def get():
    with open(keys.trello.path, "r") as file:
        board_id = file.read()
    url = f"https://api.trello.com/1/boards/{board_id}"
    response = requests.get(url, headers=keys.trello.headers, params=keys.trello.data)
    assert response.status_code == 200
get()

def delete():
    with open(keys.trello.path, "r") as file:
        board_id = file.read()
    url = f"https://api.trello.com/1/boards/{board_id}"
    response = requests.delete(url, params=keys.trello.data)
    assert response.status_code == 200
delete()

