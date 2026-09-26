numbers = [2, 5, 2, 8, 5, 2, 9, 5]
numbers_new = {}
for num in numbers:
    if num in numbers_new:
        numbers_new[num] +=1
    else:
        numbers_new[num] = 1
print(numbers_new)