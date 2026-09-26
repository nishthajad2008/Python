student = {
    "name": "Alex",
    "marks": 85,
    "grade": "A"
}
req_key = input("Enter information to find: ")
print(student.get(req_key,"Key not found."))
