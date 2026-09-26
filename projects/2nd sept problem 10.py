current_age = int(input("Enter your current age: "))
years = int(input("Enter years into the future: "))
future_age = current_age + years
future_age_months = future_age*12
if_65 = future_age >= 65
print(f"Your age after {years} years will be {future_age} years old")
print(f"Your future age in months will be {future_age_months} months")
print(f"Will you be at least 65? {if_65}")