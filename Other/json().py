import json
data = {
    "president":{
        "name" : "Zaphod Beeblebrox",
        "species" : "Betelgeusian"
    }
}

print(type(data))
data1 = json.dumps(data)
print(type(data1))
data2 = json.load(data1)
print(type(data2))