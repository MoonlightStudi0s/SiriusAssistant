import json


filename = 'users_data.json'


def open_data():
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except:
        return dict()


def save_data(users_data):
    with open(filename, "w") as f:
        json.dump(users_data, f)

