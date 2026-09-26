num = int(input("Enter an positive integer: "))
if num <= 0:
    raise ValueError ("Integer to be positive only.")
divisor = 2
found = True
while divisor*divisor <= num:
    if num % divisor == 0:
        found = False
        break
    divisor +=1
if found:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")