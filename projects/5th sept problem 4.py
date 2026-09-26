n = int(input("Enter a positive integer: "))
if n <= 0:
    raise ValueError ("Integer to be positive only.")
for num in range(n,0,-1):
    if num%3==0:
        continue
    print(num)