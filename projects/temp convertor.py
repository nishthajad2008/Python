# temperature convertor

unit = input("Is temperature in Celsius or Fahrenheit? (C/F) ")
temperature = float(input("What is the temperature?" ))
if unit == "C":
    temperature = (temperature * 1.8) + 32
    unit = "F"
    type= "Fahrenheit"
elif unit == "F":
    temperature = (temperature -32)/1.8
    unit = "C"
    type= "Celsius"
else:
    print(f"{unit} is not a valid unit")
print(f"The temperature in {type} is {temperature} {unit}")