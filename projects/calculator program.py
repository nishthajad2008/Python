#python calculator

operator = input("What operator would you like to use?(+ , - , * ,/) ")
number1 = float(input("Enter the first number "))
number2 = float(input("Enter the second number "))
if operator == "+":
    print(round(number1 + number2, 3))
elif operator == "-":
    print(round(number1 - number2, 3))
elif operator == "*":
    print(round(number1 * number2, 3))
elif operator == "/":
    print(round(number1 / number2, 3))
else:
    print("Operator not supported")
