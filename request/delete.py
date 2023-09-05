import requests
import keys.trello

def delete():

    with open("E:/PythonProjects/TrelloAPI/request/board_id.txt", "r") as file:
        board_id = file.read()

    url = f"https://api.trello.com/1/boards/{board_id}"

    response = requests.delete(url, params=keys.trello.data)

    if response.status_code == 200:
        print("Board deleted succesfully!")
    else:
        print("I can't delete this board, check it!")

    assert response.status_code == 200


delete()

