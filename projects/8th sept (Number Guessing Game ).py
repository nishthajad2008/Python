secret_number = 9
num = int(input("Enter an positive integer: "))
if num <= 0:
    raise ValueError ("Integer to be positive only.")
while num != secret_number:
    if num > secret_number:
        print("Too high, go a bit lower")
    elif num < secret_number:
        print("Too low, try a bit higher.")
    num = int(input("Try Again: "))
print("You are right")