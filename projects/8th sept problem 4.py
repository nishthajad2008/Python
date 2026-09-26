original = int(input("Enter an positive integer: "))
num = original
if original <= 0:
    raise ValueError ("Integer to be positive or zero only.")
number = 0
while num > 0:
    x = num%10
    num//=10
    number = number*10 + x
if number == original:
    print(f"{original} is a palindrome")
else:
    print(f"{original} is not a palindrome")