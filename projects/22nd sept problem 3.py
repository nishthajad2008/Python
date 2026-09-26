students = {
        "Alice": 85,
        "Bob": 72
    }
def update_mark(students, name, new_mark):
    if name in students:
        students[name] = new_mark
    else:
        print("Student not found.")
(update_mark(students, "Alice", 95))
print(students)