students = {
    "Alice": {"math": 85, "python": 92, "physics": 78},
    "Bob": {"math": 72, "python": 68, "physics": 81},
    "Charlie": {"math": 95, "python": 88, "physics": 91},
    "David": {"math": 60, "python": 75, "physics": 70}
}
count = 0
sub_1 = 0
high_name = ""
high_avg = 0
for name , info in students.items():
    for subject, marks in info.items():
        count += marks
        sub_1 +=1
    average = count / sub_1
    if average > high_avg:
        high_avg = average
        high_name = name
    count = 0
    sub_1 = 0
print(f"Highest average: {high_name}")
print(f"Average: {high_avg:.2f}")
