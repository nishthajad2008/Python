num = int(input("Enter a number: "))
numbers = [2, 5, 2, 8, 5, 2, 9, 5]
count = 0
if num not in numbers:
    print(f"{num} is not the list.")
for element in numbers:
    if element == num:
        count += 1
print(f"{num} appears {count} times.")