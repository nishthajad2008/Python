num = int(input("Enter an positive integer: "))
if num <= 0:
    raise ValueError ("Integer to be positive and zero only.")
digit  = int(input("Enter a number from 0 to 9: "))
if not 0 <= digit <= 9:
    raise ValueError("Digit to be between 0 and 9 only.")
count = 0
while num > 0:
    x = num%10
    num //=10
    if x== digit:
        count +=1
print(f"{digit} appears {count} times.")
