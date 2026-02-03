'''
Create a terinal script. It should:
1. Accept a JSON filename as the first argument
2. Accept an age limit as the second argument
3. Load the JSON
4. Print only users older than the given age
'''

"""
import sys
import json

extension = ".json"
filename = sys.argv[1]
age = int(sys.argv[2])

if extension not in filename:
    print("File typ is not supported - must be .json")

with open(filename, "r") as file:
    data = json.load(file)

filtered_users = [ user for user in data["users"] if user["age"] > age ]

for user in filtered_users:
    print(user) """


# ----------------
# The pro version:
# ----------------

import sys
import json

# --- Argument validation ---
if len(sys.argv) < 3:
    print("Usage: python filter_users.py <file.json> <age>")
    sys.exit(1)

filename = sys.argv[1]
age_limit = int(sys.argv[2])

# --- File extension check ---
if not filename.endswith(".json"):
    print("Error: File type not supported. Must be a .json file.")
    sys.exit(1)

# --- Load JSON ---
with open(filename, "r") as file:
    data = json.load(file)

# --- Filter users ---
filtered_users = [
    user for user in data["users"]
    if user["age"] > age_limit
]

# --- Output ---
for user in filtered_users:
    print(f"{user['name']} ({user['age']}) from {user['city']}")
