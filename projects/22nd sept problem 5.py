students = {
    "Alice": {"math": 85, "python": 92, "physics": 78},
    "Bob": {"math": 72, "python": 68, "physics": 81},
    "Charlie": {"math": 95, "python": 88, "physics": 91},
    "David": {"math": 60, "python": 75, "physics": 70}
}
list_1 = []
count = 0
count_1 = 0
for name , info in students.items():
    for subject, marks in info.items():
        count += marks
    if     