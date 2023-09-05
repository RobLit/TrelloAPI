import requests
import keys.trello

def create():
    url = "https://api.trello.com/1/boards/"
    data = {
        'key': keys.trello.key,
        'token': keys.trello.token,
        'name': 'new_board'
    }
    response = requests.post(url, params=data)
    data = response.json()
    board_id = data['id']
    with open("E:/PythonProjects/TrelloAPI/request/board_id.txt", "w") as file:
        file.write(board_id)
    assert response.status_code == 200
create()

def get():
    with open("E:/PythonProjects/TrelloAPI/request/board_id.txt", "r") as file:
        board_id = file.read()
    url = f"https://api.trello.com/1/boards/{board_id}"
    headers = {
        'Accept': "application/json"
    }
    response = requests.get(url, headers=headers, params=keys.trello.data)
    assert response.status_code == 200
get()

def delete():
    with open("E:/PythonProjects/TrelloAPI/request/board_id.txt", "r") as file:
        board_id = file.read()
    url = f"https://api.trello.com/1/boards/{board_id}"
    response = requests.delete(url, params=keys.trello.data)
    assert response.status_code == 200
delete()

def get_id_list():
    url = f"https://api.trello.com/1/boards/{keys.trello.id}/lists"
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, params=keys.trello.data)
    query = response.json()
    keys.trello.id_value = query[0]['id']
get_id_list()

def get_id_list2():
    with open("E:/PythonProjects/TrelloAPI/request/board_id.txt", "r") as file:
        board_id = file.read()
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, params=keys.trello.data)
    query = response.json()
    keys.trello.fst = query[0]['id']
    keys.trello.snd = query[1]['id']
    keys.trello.trd = query[2]['id']
get_id_list()
