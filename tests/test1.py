from request import crud
import keys.trello
import requests
import pytest
import json


def test_change_name():
    crud.create()
    with open(keys.trello.path, "r") as file:
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
    with open(keys.trello.path, "r") as file:
        board_id = file.read()
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    data = {
        'name': 'new_list'
    }
    response = requests.post(url, headers=keys.trello.headers, params=keys.trello.data, data=data)
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
    id = {
        'idList': keys.trello.fst,
        'name': 'Test_card'
    }
    response = requests.post(url, headers=keys.trello.headers, data=id, params=keys.trello.data)  # create new card
    assert response.status_code == 200
    crud.delete()


def test_create_label_on_a_board():
    crud.create()
    with open(keys.trello.path, "r") as file:
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


