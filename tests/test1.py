from request import crud
import keys.trello
import requests
import pytest
import json


def test_change_name():
    crud.create()
    with open("E:/PythonProjects/TrelloAPI/request/board_id.txt", "r") as file:
        board_id = file.read()
    keys.trello.url = f"https://api.trello.com/1/boards/{board_id}"
    data = {
        'name': 'kappa'
    }
    response = requests.put(keys.trello.url, params=keys.trello.data, data=data)
    json = response.json()
    name = json['name']
    crud.get()
    assert name == 'kappa'
    crud.delete()


def test_create_list():
    crud.create()
    with open("E:/PythonProjects/TrelloAPI/request/board_id.txt", "r") as file:
        board_id = file.read()
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    headers = {
        "Accept": "application/json"
    }
    data = {
        'name': 'new_list'
    }
    response = requests.post(url, headers=headers, params=keys.trello.data, data=data)
    json = response.json()
    name = json['name']
    assert response.status_code == 200
    crud.get()
    assert name == 'new_list'
    crud.delete()


def test_get_first_list():
    crud.create()
    crud.get_id_list2()
    url = f"https://api.trello.com/1/lists/{keys.trello.fst}" #get id of first list
    response = requests.get(url, params=keys.trello.data)
    assert response.status_code == 200
    crud.delete()


def test_get_second_list():
    crud.create()
    crud.get_id_list2()
    url = f"https://api.trello.com/1/lists/{keys.trello.snd}" #get id of second list
    response = requests.get(url, params=keys.trello.data)
    assert response.status_code == 200
    crud.delete()


def test_get_third_list():
    crud.create()
    crud.get_id_list2()
    url = f"https://api.trello.com/1/lists/{keys.trello.trd}" #get id of third list
    response = requests.get(url, params=keys.trello.data)
    assert response.status_code == 200
    crud.delete()


def test_update_1st_list():
    crud.create()
    crud.get_id_list2()
    url = f"https://api.trello.com/1/lists/{keys.trello.fst}"
    data = {
        'name': 'updated_name'
    }
    response = requests.put(url, data=data, params=keys.trello.data)
    name = response.json()['name']
    assert name == 'updated_name'
    crud.delete()


def test_create_card():
    crud.create()
    crud.get_id_list2()
    url = "https://api.trello.com/1/cards"
    headers = {
        "Accept": "application/json"
    }
    id = {
        'idList': keys.trello.fst,
        'name': 'Test_card'
    }
    response = requests.post(url, headers=headers, data=id, params=keys.trello.data)  # create new card
    assert response.status_code == 200
    crud.delete()


def test_create_label_on_a_board():
    crud.create()
    with open("E:/PythonProjects/TrelloAPI/request/board_id.txt", "r") as file:
        board_id = file.read()
    url = f"https://api.trello.com/1/boards/{board_id}/labels"
    data = {
        'name': 'new_label',
        'color': 'yellow'
    }
    response = requests.post(url, data=data, params=keys.trello.data)
    assert response.status_code == 200
    crud.get()
    crud.delete()


def test_create_email_board():
    crud.create()
    with open("E:/PythonProjects/TrelloAPI/request/board_id.txt", "r") as file:
        board_id = file.read()
    url = f"https://api.trello.com/1/checklists/{board_id}"
    response = requests.get(url, params=keys.trello.data)
    assert response.status_code == 200
    crud.delete()


def test_checkitem_on_checklist_flow():
    crud.create()
    crud.get_id_list2()
    url = "https://api.trello.com/1/cards"
    headers = {
        "Accept": "application/json"
    }
    id = {
        'idList': keys.trello.fst,
        'name': 'Test_card'
    }
    response = requests.post(url, headers=headers, data=id, params=keys.trello.data)  # create new card
    idCard = response.json()['id']
    assert response.status_code == 200
    url = "https://api.trello.com/1/checklists"
    data = {
        'idCard': idCard
    }
    response = requests.post(url, data=data, params=keys.trello.data)  # create a checklist
    assert response.status_code == 200
    idChecklist = response.json()['id']
    url = f"https://api.trello.com/1/checklists/{idChecklist}/checkItems"
    data = {
        'name': 'test'
    }
    response = requests.post(url, data=data, params=keys.trello.data)
    idCI = response.json()['id']
    assert response.status_code == 200
    url = f"https://api.trello.com/1/checklists/{idChecklist}/checkItems/{idCI}"
    response = requests.get(url, params=keys.trello.data) #get checkitem
    assert response.json()['name'] == 'test'
    response = requests.delete(url, params=keys.trello.data) #delete checkitem
    assert response.status_code == 200
    response = requests.get(url, params=keys.trello.data)  # get checkitem
    assert response.status_code == 404
    crud.delete()