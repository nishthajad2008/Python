numbers = [2, 5, 2, 8, 5, 9, 8, 8]
set1 = set()
for num in numbers:
    if numbers.count(num) > 1:
        set1.add(num)
print(set1)