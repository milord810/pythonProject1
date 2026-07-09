import json


def read_json(filename):
    try:
        with open (filename, encoding='UTF-8') as file:
            data = json.load(file)
            if type(data) is list:
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


if __name__ == "__main__":
    print(read_json("../data/operations.json"))
