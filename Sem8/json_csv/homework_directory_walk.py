import csv
import json
import os

CSV_HEADER = ("name", "type", "size")


def export_current_folder_info(path, json_name="folder_info.json", csv_name="folder_info.json"):
    all_dirs = tuple(os.walk(path))
    objs = list()
    for obj in all_dirs:
        current_folder = {"name": obj[0], "type": "directory", "size": 0, "files_inside": list()}
        for filename in obj[2]:
            size = os.stat(os.path.join(obj[0], filename)).st_size
            current_folder["size"] += size
            current_folder["files_inside"].append({"name": filename, "type": "file", "size": size})
        objs.append(current_folder)

    with open("folder_info.json", 'w', encoding='utf-8') as f:
        json.dump(objs, f, indent=3)

    with open("folder_info.csv", 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(CSV_HEADER)
        for folder in objs:
            wr.writerow((folder['name'], folder['type'], folder['size']))
            for file in folder['files_inside']:
                wr.writerow((folder['name'] + os.path.sep + file['name'], file['type'], file['size']))


if __name__ == '__main__':
    export_current_folder_info("..")
