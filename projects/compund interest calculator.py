# Python compound interest calculator
# final amount = initial principle balance( 1+(interest rate/n)^number of time periods elapsed

principle_amount = 0
rate = 0
time = 0

while principle_amount <= 0:
    principle_amount = float(input("Enter a principle amount: "))
    if principle_amount <= 0:
        print("principle cant be less than or equal to zero)")
print(principle_amount)

while rate <= 0:
    rate = float(input("Enter a rate: "))
    if rate <= 0:
        print("rate cant be less than or equal to zero")
print(rate)

while time <= 0:
    time = int(input("Enter the time period (years): "))
    if time <= 0:
        print("time cant be less than or equal to zero")
print(time)
total = principle_amount*((1 + rate/100 )**time)
print(f"Balance after {time} year/s: ${total:.2f}")