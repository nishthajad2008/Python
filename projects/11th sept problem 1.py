student = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 64
}
highest_stu = ""
highest_mark = 0
for name,mark in student.items():
    if mark > highest_mark:
        highest_mark = mark
        highest_stu = name
print(f"Highest: {highest_stu}")
print(f"Mark: {highest_mark}")