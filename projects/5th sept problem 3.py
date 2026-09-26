n = int(input("Enter a positive integer: "))
if n <= 0:
    raise ValueError ("Integer to be positive only.")
total =0
for num in range(1,n+1):
    if num%3==0:
        total+=num
print(f"Sum: {total}")