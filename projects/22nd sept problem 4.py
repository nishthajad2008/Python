students = {
    "Alice": 85,
    "Bob": 72
}
def find_student(students, name):
    if name in students:
        return students[name]
    else:
        return None
print(find_student(students, "Alice"))