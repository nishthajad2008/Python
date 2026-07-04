# If = Do some code only IF some condition is True
#      ELSE do something else

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
elif age >=13:
    print("You are an minor")
else:
    print("You are a child")

#Simple convo
response = (input("Would you like some food? (yes / no)"))
if response == "yes":
    print(input("What would you like to have?"))
    print(input("Okay, coming with it right back"))
else:
    print("Okay,no worries. Have a good day")

# in terms of true and false
for_sale = True
if for_sale:
    print(" This item is for sale")
else:
    print(" This item is not for sale")