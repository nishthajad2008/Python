#conditional expression = A one line shortcut for the if-else statement(ternary operator)
#                         print or assign one of two values based on a condition
#                         x is condition else y (formula)

number = 5
a = 7
b = 8
age = 18
print( "positive" if number > 0 else "negative" )
print("even" if number % 2 == 0 else "odd")
max_num = a if a > b else b
print(max_num)
min_num = a if a < b else b
print(min_num)
print("adult" if age >= 18 else "teen")
