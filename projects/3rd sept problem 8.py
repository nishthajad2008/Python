age = int(input("Enter your age: "))
student = input("Are you a student (Yes or No): ")
if age < 5:
    print("Ticket price: ₹0")
elif age <= 12:
    print("Ticket price: ₹100")
elif age <= 17:
    if student.lower() == "yes":
        print("Ticket price: ₹100")
    else:
        print("Ticket price: ₹150")
elif age <= 59:
    if age <= 25 and student.lower() == "yes":
        print("Ticket price: ₹200")
    else:
        print("Ticket price: ₹250")
else:
    print("Ticket price: ₹120")
