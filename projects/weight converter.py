# Python weight converter

weight = float(input("Enter your weight:"))
unit = input("Kilogram or Pounds?(K or P)")
if unit == "P":
    weight = weight/2.205
    unit = "lbs"
    print(f"Your weight in kilogram is {weight} kg")
elif unit == "K":
    weight = weight * 2.205
    unit = "kg"
    print(f"Your weight in Pounds is {weight} lbs")
else:
    print(f"{unit} is not a valid unit")