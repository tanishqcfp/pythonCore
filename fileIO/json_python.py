import json

#convert json string format into python dict

json_data = '{"name": "Tanishq", "age": 21}'

data = json.loads(json_data)

print(data)
print(type(data))


# convert json file into python object
with open("data1.json","r") as f:
    data = json.load(f)

print(data)
print(type(data))