students = {
    "Alice": {
        "marks": 85,
        "age": 20
    },
    "Bob": {
        "marks": 72,
        "age": 21
    },
    "Charlie": {
        "marks": 91,
        "age": 19
    }
}
for name, info in students.items():
    print(f"{name} is {info["age"]} years old")