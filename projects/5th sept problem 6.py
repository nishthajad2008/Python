n = int(input("Enter a positive integer: "))
if n <= 0:
    raise ValueError ("Integer to be positive only.")
found = False
for num in range(1,n+1):
    if num%4==0 and num%6==0:
        found = True
        break
if found:
    print(f"First number divisible by both 4 and 6: {num}")
else:
    print("No such number was found.")