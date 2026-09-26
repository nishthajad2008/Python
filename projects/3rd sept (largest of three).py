num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 == num2 and num2 == num3:
    print("All three are equal")
elif num1 >= num2 and num1 >= num3:
    if num1 == num2 or num1 == num3:
        print(f"{num1} is tied for the largest")
    else:
        print(f"{num1} is  largest")
elif num2 >= num1 and num2 >= num3:
    if num2 == num1 or num2 == num3:
        print(f"{num2} is tied for largest")
    else:
        print(f"{num2} is largest")
else:
    print(f"{num3} is the largest")
