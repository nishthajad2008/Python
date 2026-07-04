# while loop = execute some code WHILE some condition remains true
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")
#exercise 2
number = int(input("Enter a num between 1 - 10: "))

while int(number)< 1 or int(number) > 10:
    print("You did not enter a valid number")
    number = input("Enter a number between 1 - 10: ")

print(f"You entered {number}")