marks = {
    "Alice": 85,
    "Bob": 32,
    "Charlie": 67,
    "David": 91,
    "Emma": 45,
    "Frank": 28
}
dict_1 ={}
for key,value in marks.items():
    if value > 40:
        dict_1[key] = value
print(dict_1)