number = int(input("Enter the number: "))
count = 0
for i in range(number+1):
    count += i
    print(f"The sum is {count}")