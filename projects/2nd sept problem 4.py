bill = float(input("Bill amount: "))
tip = float(input("Tip to give (percentage of bill): "))
num_people = int(input("Number of people: "))
tip_total = bill * (tip/100)
total = bill + tip_total
each_pay = total / num_people
print(f"Each person pays ${each_pay:.2f}")