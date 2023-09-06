key = '1f3181b7431debbb306838d1df03f924'
token = 'ATTA3248403af8f3f93207988df212dc158815bdde52c1723803092b2d9dc5774f27276D859F'

path = 'E:/PythonProjects/TrelloAPI/request/board_id.txt'

data = {
  'key': key,
  'token': token
}

headers = {
  "Accept": "application/json"
}

with open(path, "r") as file:
  board_id = file.read()

url = f"https://api.trello.com/1/boards/{board_id}"

id_value = None
fst = None
snd = None
trd = None