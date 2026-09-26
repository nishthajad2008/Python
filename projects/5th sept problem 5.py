n = int(input("Enter a positive integer: "))
total = 1
for factorial in range(1,n+1):
    total *= factorial
print(f"{n}!={total}")