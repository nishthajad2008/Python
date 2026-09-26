num = int(input("Enter an positive integer: "))
if num <= 0:
    raise ValueError ("Integer to be positive only.")
largest = 0
while num > 0:
    x = num%10
    num//=10
    if x > largest:
        largest = x
print(f"{largest} is the largest digit")



