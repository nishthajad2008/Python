students = {}
no_of_students = int(input("Enter number of students: "))
count = 0
while count < no_of_students:
       name = input("Enter the student name: ")
       marks = int(input("Enter the student mark: "))
       count += 1
       students[name] = marks
# to print list
for name, mark in students.items():
    print(f"{name}: {mark}")
#search
names = input("Enter student name: ")
if names in students:
    print(f"{names}'s mark: {students[names]}")
elif names not in students:
    print(f"{names} not found.")
#update
stu_name = input("Enter student name: ")
new_mark = int(input("Enter new mark: "))
if stu_name in students:
    students[stu_name] = new_mark
else:
    print(f"{stu_name} not found.")
#remove
remove_stu = input("Enter student name to remove: ")
if remove_stu in students:
    students.pop(f"{remove_stu}")
else:
    print(f"{remove_stu} not found.")
#highest scorer
highest_student = list(students.keys())[0]
highest_score = students[highest_student]
for key,value in students.items():
    if value > highest_score:
        highest_score = value
        highest_student = key
print(f"Highest scorer: {highest_student}")
print(f"Mark: {highest_score}")
#average
summation = 0
for value in students.values():
    summation += value
average = summation / len(students)
print(f"Class Average: {average}")
# pass or fail
passed = 0
failed = 0
for value in students.values():
    if value >= 40:
        passed += 1
    else:
        failed += 1
print(f"Passed: {passed}")
print(f"Failed: {failed}")