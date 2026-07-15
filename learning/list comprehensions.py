even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)
# This example creates a new empty list called even_numbers and loops through a sequence of numbers between 0 and 20.
# Inside the loop, there's a condition that checks if the current number has a remainder of 0 when divided by 2.
# This is used to determine if the number is even.
# If the condition is True, then the current num is appended at the end of the even_numbers list.
# Finally, we print the even_numbers list to the console.

even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
#the concise way for the same code and explanation

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']
#The filter() function is used to select elements from an iterable that meet a specific condition.
#The filter() function accepts a function and an iterable for its arguments

celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]
#Just like the filter() function, map() accepts a function and an iterable for its arguments.
# The to_fahrenheit function takes a temperature and converts it from Celsius to Fahrenheit.