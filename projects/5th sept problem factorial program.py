num = int(input("Enter an positive integer: "))
if num < 0:
    raise ValueError ("Integer to be positive only.")
total = 1
for factorial in range(1,num+1):
    total *= factorial
print(f"{num}! = {total}")

