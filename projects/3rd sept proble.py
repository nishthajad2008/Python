num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num2} is greater than {num1}.")
else:
    print(f"first number ({num1}) and second number ({num2}) are equal.")