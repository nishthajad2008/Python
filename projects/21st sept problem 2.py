marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 64,
    "Emma": 38
}
count = 0
for value in marks.values():
    if value >= 70:
        count +=1
print(f"{count} students scored above or equal to 70.")