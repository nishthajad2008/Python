def square(num):
    return num ** 2

print(square(4)) # 16
# when it comes to working with high order functions like map() and filter(), you can use an anonymous inline function.
#This is where lambda functions come in.

numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
#In this example, we have a list of numbers and want to create a new list of even numbers.
#So we pass in a lambda function as one of the arguments to the filter() function to get a new list containing the numbers 2 and 4.
#not a good practice to assign a lambda function to a variable
# If you are dealing with a single inline expressions, then you might consider using a lambda function.
# Otherwise, using a regular function would be the way to go.

