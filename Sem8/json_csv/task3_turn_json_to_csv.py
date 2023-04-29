import csv
import json

HEADER = ['Access_level', 'User_ID', 'User_name']

def export_json_to_csv(json_filename, csv_filename):
    with open(json_filename, 'r', encoding='utf-8') as f:
        levels = json.load(f)
    with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
        wr = csv.writer(f, dialect='excel')
        wr.writerow(HEADER)
        for level, users in levels.items():
            for user in users:
                for userid, name in user.items():
                    wr.writerow((level, userid, name))


if __name__ == '__main__':
    export_json_to_csv("../data.json", "../data.csv")