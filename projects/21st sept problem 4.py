marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 64,
    "Emma": 88
}
highest_score = list(marks.values())[0]
highest_name = list(marks.keys())[0]
for key,value in marks.items():
    if value > highest_score:
        highest_score = value
        highest_name = key
print(f"Highest Student: {highest_name}")
print(f"Highest mark: {highest_score}")