import json

data = {"name": "John", "age": 30}

with open("data.json", "w") as file:
    json.dump(data, file)
