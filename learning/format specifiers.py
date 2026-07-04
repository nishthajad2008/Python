# format specifiers = {value:flags} format a value based on what
#                              flags are inserted
# :.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = -3.14159
price2 = -987.65
price3 = 12908.34

print(f"price 1 is ${price1:.2f}") # number of decimals to be displayed
print(f"price 2 is ${price2:.8}") #spaces or blanks to display the number ( run and count the number of spaces to understand)
print(f"price 3 is ${price3:07}") #zero padded that is instead of blanks, there will be zero to fulfil the spaces
print(f"price 1 is ${price1:<7}")# left justifier that is all the blanks will be after the digits
print(f"price 2 is ${price2:>7}")#right justifier that is all the blanks will be before the digits
print(f"price 3 is ${price3:^9}")#center justifier that is there be equal space on both the side of the digits
print(f"price 1 is ${price1:+}")#to display positive values
print(f"price 2 is ${price2: }")# to add space before positive numbers
print(f"price 3 is ${price3:,}")#to display comma (run the program to understand)
# you can use multiple flags for one line ex:
print(f"price 3 is ${price3:+,.2f}")