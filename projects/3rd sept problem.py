age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (Yes or No): ")
if age >=18 and citizen.lower() == "yes":
    print("Eligible to vote")
else:
    print("Not eligible to vote")