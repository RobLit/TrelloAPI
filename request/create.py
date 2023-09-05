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
    #print(response.text)

    #url = f"https://api.trello.com/1/boards/{board_id}/lists"
    #response = requests.get(url, params=keys.trello.data)
    #data2 = response.json()
    #xy = data2['idBoard']
    #print(response.json())

create()

