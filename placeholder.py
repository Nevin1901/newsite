import json
import requests

class Person:
    def __init__(self, _id, title):
        self._id = _id
        self.title = title

response = requests.get("https://jsonplaceholder.typicode.com/posts")
todos = json.loads(response.text)


people = []

for guy in todos:
    people.append(Person(guy["userId"], guy["title"]))

print(people[0]._id)
