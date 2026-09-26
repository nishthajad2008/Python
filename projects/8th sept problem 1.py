num = int(input("Enter an positive integer: "))
if num <= 0:
    raise ValueError ("Integer to be positive only.")
number = 0
while number < num:
    number += 1
    if number%2 == 0:
        continue
    print(number)