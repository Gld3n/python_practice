import json

person = {
    "name": "Robert",
    "age": 18,
    "studies": "Engineering",
    "hasCapybara": False
}

person_json = json.dumps(person, indent=4)
print(person_json)

with open("testing.json", "w") as file:
    json.dump(person, file, indent=2)
    
person_temp = json.loads(person_json)
print(person_temp)