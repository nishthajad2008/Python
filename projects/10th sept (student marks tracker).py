no_of_student = int(input("Enter number of students: "))
marks = []
while no_of_student:
    mark = int(input("Enter marks: "))
    marks.append(mark)
    if len(marks) == no_of_student:
        break
print(marks)
highest = marks[0]
lowest = marks[0]
passed = 0
failed = 0
for num in marks:
    if num > highest:
        highest = num
    if num < lowest:
        lowest = num
    if num >= 40:
        passed += 1
    else:
        failed += 1
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
summation = 0
for summ in marks:
    summation +=summ
average = summation/len(marks)
print(f"Average: {average:.2f}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")