import json
import os.path


def add_to_json(data_filename):
    levels = dict()
    id_set = set()
    if os.path.exists(data_filename):
        with open(data_filename, 'r', encoding='utf-8') as f:
            levels = json.load(f)
            id_set = {userid for level, users in levels.items() for user in users for userid, name in user.items()}
    name = input("Enter name: ")
    id = input("Enter ID: ")
    while id in id_set:
        id = input("This ID already exists. Enter unique ID: ")
    access_level = input("Enter access level (1-7): ")
    levels.setdefault(access_level, list()).append({id: name})
    with open(data_filename, 'w', encoding='utf-8') as f:
        json.dump(levels, f, indent=3, ensure_ascii=False, sort_keys=True)


if __name__ == '__main__':
    while True:
        add_to_json("../data.json")
