student = {
    "name": "Alex",
    "marks": 85
}
student["age"] = 20
print(student.get("marks"))
student["marks"] = 92
student.pop("age")
print(student)