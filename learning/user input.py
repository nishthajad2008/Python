#input() = A function that prompts the user to enter data
#          Returns the entered data as a string.

name = input("What is your name?")
print(f"Hello {name}")

#exercise 1 rectangle area calc
length = int(input("length of the rectangle (in metres)?"))
width = int(input("width of the rectangle (in metres)?"))
area = length * width
print(f"Area of the rectangle is {area} m^2")

#exercise 2 shopping cart program
item = input("What is your item?")
price = float(input("price of the item?"))
quantity = int(input("quantity of the item?"))
total_price = price * quantity
print(f"Total price is ${total_price}")