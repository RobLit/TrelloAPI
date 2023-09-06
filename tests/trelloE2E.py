from request import crud
import keys.trello
import requests
import pytest
import json


def test_E2E_basic_board_manipulation():
    crud.create()
    crud.get()
    with open(keys.trello.path, "r") as file:
        board_id = file.read()
    url = f"https://api.trello.com/1/boards/{board_id}"
    data = {
        'name': 'updated_name'
    }
    response = requests.put(url, data=data, params=keys.trello.data) #update a board
    assert response.status_code == 200
    response = requests.get(url, headers=keys.trello.headers, params=keys.trello.data) #get a board
    assert response.json()['name'] == 'updated_name'
    crud.delete()


def test_E2E_board_manipulation():
    crud.create() #create a board
    with open(keys.trello.path, "r") as file:
        board_id = file.read()
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    data = {
        'name': 'new_list'
    }
    response = requests.post(url, headers=keys.trello.headers, params=keys.trello.data, data=data) #create a list on board
    assert response.status_code == 200
    crud.get_id_list2()
    url = f"https://api.trello.com/1/lists/{keys.trello.fst}"
    data = {
        'name': 'updated_name'
    }
    response = requests.put(url, params=keys.trello.data, data=data) #update a list
    assert response.status_code == 200
    url = f"https://api.trello.com/1/lists/{keys.trello.fst}"
    response = requests.get(url, headers=keys.trello.headers, params=keys.trello.data)  #get list on a board
    name = response.json()['name']
    assert name == 'updated_name'
    assert response.status_code == 200
    url = f"https://api.trello.com/1/lists/{keys.trello.fst}/closed"
    data = {
        'value': 'true'
    }
    response = requests.put(url, data=data, params=keys.trello.data) #archive a list
    assert response.status_code == 200
    data = {
        'value': 'false'
    }
    response = requests.put(url, data=data, params=keys.trello.data) #unarchive a list
    assert response.status_code == 200
    crud.delete() #delete a board


def test_E2E_basic_card_manipulation():
    crud.create()
    crud.get_id_list2()
    url = "https://api.trello.com/1/cards"
    id = {
        'idList': keys.trello.fst,
        'name': 'Test_card'
    }
    response = requests.post(url, headers=keys.trello.headers, data=id, params=keys.trello.data)  #create new card
    assert response.status_code == 200
    id = response.json()['id']
    url = f"https://api.trello.com/1/cards/{id}"
    response = requests.get(url, headers=keys.trello.headers, params=keys.trello.data)  #get a card
    assert response.status_code == 200
    assert response.json()['name'] == 'Test_card'
    data = {
        'name': 'Updated_name'
    }
    response = requests.put(url, headers=keys.trello.headers, data=data, params=keys.trello.data)  #update a card
    assert response.status_code == 200
    response = requests.get(url, headers=keys.trello.headers, params=keys.trello.data)  #get updated card
    assert response.json()['name'] == 'Updated_name'
    response = requests.delete(url, params=keys.trello.data) #delete a card
    assert response.status_code == 200
    response = requests.get(url, headers=keys.trello.headers, params=keys.trello.data) #get deleted card
    assert response.status_code == 404
    crud.delete()


def test_E2E_label_manipulation():
    crud.create()
    with open(keys.trello.path, "r") as file:
        board_id = file.read()
    url = "https://api.trello.com/1/labels"
    data = {
        'name': 'new_label',
        'color': 'green',
        'idBoard': board_id
    }
    response = requests.post(url, data=data, params=keys.trello.data) #create a label
    assert response.status_code == 200
    id_label = response.json()['id']
    color = response.json()['color']
    name = response.json()['name']
    url = f"https://api.trello.com/1/labels/{id_label}"
    response = requests.get(url, params=keys.trello.data) #get a label
    assert response.status_code == 200
    assert color == 'green'
    assert name == 'new_label'
    response = requests.delete(url, params=keys.trello.data) #delete a label
    assert response.status_code == 200
    response = requests.get(url, params=keys.trello.data) #get deleted label
    assert response.status_code == 404
    crud.delete()


def test_E2E_board_checklist():
    crud.create()
    crud.get_id_list2()
    url = "https://api.trello.com/1/cards"
    data = {
        'idList': keys.trello.fst #get id from first list on a board
    }
    response = requests.post(url, headers=keys.trello.headers, data=data, params=keys.trello.data) #create a new card
    idCard = response.json()['id']
    url = "https://api.trello.com/1/checklists"
    data = {
        'idCard': idCard
    }
    response = requests.post(url, data=data, params=keys.trello.data) #create a checklist
    assert response.status_code == 200
    idChecklist = response.json()['id']
    url = f"https://api.trello.com/1/checklists/{idChecklist}"
    response = requests.delete(url, params=keys.trello.data) #delete checklist
    assert response.status_code == 200
    response = requests.get(url, params=keys.trello.data) #get deleted checklist
    assert response.status_code == 404
    crud.delete()


def test_E2E_attachments():
    crud.create() #create a board
    crud.get_id_list2() #get id list of created board
    url = "https://api.trello.com/1/cards"
    data = {
        'idList': keys.trello.fst
    }
    response = requests.post(url, headers=keys.trello.headers, data=data, params=keys.trello.data)
    id = response.json()['id']
    url = f"https://api.trello.com/1/cards/{id}/attachments"
    data = {
        'url': 'https://www.google.com'
    }
    response = requests.post(url, headers=keys.trello.headers, data=data, params=keys.trello.data) #create attachment on card
    assert response.status_code == 200
    idAtt = response.json()['id']
    url = f"https://api.trello.com/1/cards/{id}/attachments/{idAtt}"
    assert response.status_code == 200
    assert response.json()['url'] == 'https://www.google.com' #validation
    response = requests.delete(url, params=keys.trello.data) #delete an attachment
    assert response.status_code == 200
    response = requests.get(url, headers=keys.trello.headers, params=keys.trello.data) #get deleted attachment
    assert response.status_code == 400 #should have 400 status code
    crud.delete() #delete board


def test_E2E_comment_flow():
    crud.create() #create a new board
    crud.get_id_list2() #get id number of first list from created board
    url = "https://api.trello.com/1/cards"
    data = {
        'idList': keys.trello.fst
    }
    response = requests.post(url, headers=keys.trello.headers, data=data, params=keys.trello.data) #create a new card
    idCard = response.json()['id']
    assert response.status_code == 200
    url = f"https://api.trello.com/1/cards/{idCard}/actions/comments"
    data = {
        'text': "New Comment"
    }
    response = requests.post(url, headers=keys.trello.headers, data=data, params=keys.trello.data) #add a new comment
    idCom = response.json()['id']
    assert response.status_code == 200
    url = f"https://api.trello.com/1/actions/{idCom}/text"
    data = {
        'value': "Updated Comment"
    }
    response = requests.put(url, data=data, params=keys.trello.data) #update comment
    assert response.status_code == 200
    response = requests.delete(url, params=keys.trello.data) #delete a comment
    assert response.status_code == 200
    crud.delete()


