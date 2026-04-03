import json

# convert python dic type into json string type using dumps()

# data = {
#     "name": "Tanishq",
#     "age": 21,
#     "skills": ["Python", "SQL"]
# }
# # python treats it like dict but after converting into JSON string it treats it like a string

# json_data = json.dumps(data)


# print(json_data)
# print(type(json_data))


# write json to a file using dump()

data = {
    "name" : "tanishq",
    "age" : 22
}

with open("data1.json","w") as f:
    json.dump(data,f)

