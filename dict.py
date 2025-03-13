notes = {
    "apple": "1kg",
    "banana": 12,
    "orange" : 6 }
print(notes)

notes["orange"] = notes["orange"] + 6
del notes["apple"]
print(notes.keys())
print(notes.values())
print(notes.items())
