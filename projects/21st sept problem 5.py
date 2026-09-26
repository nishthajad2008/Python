marks = {
    "Alice": 85,
    "Bob": 42,
    "Charlie": 91,
    "David": 35,
    "Emma": 68
}
marks_new = {}
for key,value in marks.items():
    if value >= 40:
        marks_new[key] = value
print(marks_new)