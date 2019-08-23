#This file parses the data from users.json and creates an array of objects
import json

#Array of user objects
userArray = []

#User object
class user:
    def __init__(self, name, ID, admin, phrases):
        self.name = name;
        self.ID = ID;
        self.admin = admin;
        self.phrases = phrases;


with open('users.json') as f:
    data = json.loads(f.read())

print("--Importing users.json data--")
for x in data['users']:
    userArray.append(user(x['name'], x['ID'], bool(x['admin']), x['phrases']))

print("Imported", len(userArray), "users.")

