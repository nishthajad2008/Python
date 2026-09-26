weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (metres):" ))
if height <= 0 or weight <= 0:
    raise ValueError ("Height or weight cannot be zero")
bmi = weight / (height**2)
if bmi < 18.5:
    print(f"Classification: Underweight({bmi:.2f}) ")
elif bmi <= 24.9:
    print(f"Classification: Normal({bmi:.2f})")
elif bmi <= 29.9:
    print(f"Classification: Overweight({bmi:.2f})")
else:
    print(f"Classification: Obese({bmi:.2f})")
