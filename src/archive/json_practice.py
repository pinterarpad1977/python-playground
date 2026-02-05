import json

with open("/app/data/users.json", "r") as file:
    data = json.load(file)

    for user in data["users"]:
        print(f'{user["name"]} ({user["age"]}) from {user["city"]}')

young_users = [ user for user in data["users"] if user["age"] < 40 ]

with open("/app/data/young_users.json", "w") as file:
    json.dump( {"users": young_users}, file, indent=4)
    