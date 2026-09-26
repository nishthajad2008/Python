num = int(input("Enter an positive integer: "))
if num <= 0:
    raise ValueError ("Integer to be positive only.")
even = 0
odd = 0
while num > 0:
    digit = num%10
    num//=10
    if digit %2==0:
        even +=1
    if digit %2==1:
        odd +=1
print(f"Even digits: {even}")
print(f"Odd digits: {odd}")