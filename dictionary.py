#dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}
print(student)
print(type(student))
print(len(student))
print(student["name"])
print(student["age"])
print(student["grade"])

meanings = {"bat" : "used to hit",
            "ball" : "this is hit",
            "wiket" : "to be protected"
            }

print(type(meanings))
print(meanings.get("ball", "not found"))

#adding
meanings["man"] = "he is the playes"
print(meanings)

#update
meanings["man"] = "he is man of the players"
print(meanings)

meanings.pop("man")
print(meanings)

print(meanings.keys())
print(meanings.values())

print(meanings.items())