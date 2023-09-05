key = 'yourAPIKey'
token = 'yourToken'

data = {
  'key': key,
  'token': token
}

headers = {
  "Accept": "application/json"
}

with open("E:/PythonProjects/TrelloAPI/request/board_id.txt", "r") as file:
  board_id = file.read()

url = f"https://api.trello.com/1/boards/{board_id}"

id = '64ecb8da3588ab75ec30cdb4'

#id_value = None
fst = None
snd = None
trd = None