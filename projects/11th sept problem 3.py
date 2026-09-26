marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 64,
    "Emma": 38,
    "Frank": 72
}
summation = 0
count = 0
new_list = []
for name, mark in marks.items():
    summation += mark
    count +=1
average = summation / count
for name,mark in marks.items():
    if mark > average:
        new_list.append(name)
print(new_list)