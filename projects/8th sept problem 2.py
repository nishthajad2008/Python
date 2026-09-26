num = int(input("Enter an positive integer: "))
if num <= 0:
    raise ValueError ("Integer to be positive only.")
number = 0
while num > 0:
    num //= 10
    number +=1
print(number)