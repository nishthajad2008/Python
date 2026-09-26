num = int(input("Enter an positive integer: "))
if num <= 0:
    raise ValueError ("Integer to be positive only.")
for number in range(1,11):
    print(f"{num} x {number} = {num*number}")