numbers = [2, 5, 2, 8, 5, 2, 9, 8]
new_list = []
for num in numbers:
    if num not in new_list:
        new_list.append(num)
print(new_list)