my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}

for(key, value) in my_family.items():
    name = value["name"]
    age = str(value["age"])
    print(f"{name} is my {key} and {age} is years old")
