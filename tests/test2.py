from request import crud
import keys.trello
import requests
import pytest
import json


def test_create_checkitem_on_checklist_positive():
    crud.create()
    crud.get_id_list2()
    url = "https://api.trello.com/1/cards"
    id = {
        'idList': keys.trello.fst,
        'name': 'Test_card'
    }
    response = requests.post(url, headers=keys.trello.headers, data=id, params=keys.trello.data)  # create new card
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
    assert response.status_code == 200
    crud.delete()


def test_create_checkitem_on_checklist_negative1():
    crud.create()
    crud.get_id_list2()
    url = "https://api.trello.com/1/cards"
    id = {
        'idList': keys.trello.fst,
        'name': 'Test_card'
    }
    response = requests.post(url, headers=keys.trello.headers, data=id, params=keys.trello.data)  # create new card
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
        'name': ' ' #'name' should be a string of length at least 1 letter
    }
    response = requests.post(url, data=data, params=keys.trello.data)
    assert response.status_code == 400
    crud.delete()


def test_create_checkitem_on_checklist_negative2():
    crud.create()
    crud.get_id_list2()
    url = "https://api.trello.com/1/cards"
    id = {
        'idList': keys.trello.fst,
        'name': 'Test_card'
    }
    response = requests.post(url, headers=keys.trello.headers, data=id, params=keys.trello.data)  # create new card
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
        'name': '123' #'name' should be a string of length at least 1 letter
    }
    response = requests.post(url, data=data, params=keys.trello.data)
    assert response.status_code == 400
    crud.delete()


def test_checkitem_on_checklist_flow():
    crud.create()
    crud.get_id_list2()
    url = "https://api.trello.com/1/cards"
    id = {
        'idList': keys.trello.fst,
        'name': 'Test_card'
    }
    response = requests.post(url, headers=keys.trello.headers, data=id, params=keys.trello.data)  # create new card
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