friends = 10
#friends = friends + 1 (shortcut is given below)
friends += 1
#friends = friends -2
friends -= 2
#friends = friends ** 3 (raised to 3)
friends **= 3
remainder = friends % 3
print(remainder)

#built-in math functions
x = 3.14
y =-4
z= 5

result = round(x , 2) #(rounding)
print(result)
result = abs(y) #(turns into positive whole number)
print(result)
result = pow(y, 3)  #(power, y raised to 3)
print(result)
result = max(x,y,z) #(to find maximum)
print(result)
result = min(x,y,z) #(to find minimum)
print(result)

# important ones
import math
print(math.pi)
print(math.e)
result = math.sqrt(1931)
print(result)
result = math.floor(1931.333) #round down
print(result)
result = math.ceil(1931.333) #round up
print(result)

#exercise 1 calc circumference of a circle
import math
radius = float(input("Enter radius: "))
circumference = math.pi * 2 *radius
print(f"Circumference of circle is {round(circumference,2)}")

#exercise 2 calc area of a circle
import math
radius = float(input("Enter radius: "))
area = pow(radius , 2) * math.pi
print(f"Area of circle is {round(area,2)}")

#exercise 3 finding the hypotenuse of a right triangle
import math
height = float(input("Enter height of the triangle: "))
base = float(input("Enter Base of the triangle : "))
hypotenuse = pow(pow(height, 2) + pow(base, 2),0.5)
print(hypotenuse)