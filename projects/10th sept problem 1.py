numbers = [12, 7, 25, 4, 18, 9]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")