import json

def load_expenses():
    with open("data.json", "r") as file:  # with automatically closes the file after reading.
        data = json.load(file)    # json.load() reads the JSON data from the file and converts it into a Python list
        return data