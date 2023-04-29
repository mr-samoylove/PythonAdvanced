import csv
import json


def turn_csv_to_json(csv_filename, json_filename):
    users = list()
    with open(csv_filename, 'r', encoding='utf-8', newline='') as f:
        content = csv.reader(f)
        next(content)  # чтобы пропустить заголовок
        for line in csv.reader(f):
            userid = line[1].zfill(10)
            name = line[2].capitalize()
            users.append({"userid": userid, "name": name, "access_level": line[0], "hash": hash(name + userid)})
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=3)


if __name__ == '__main__':
    turn_csv_to_json("../data.csv", "../task4_data.json")
