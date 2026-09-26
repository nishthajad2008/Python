numbers = [12, 5, 8, 21, 4, 16, 7, 10]
new_list = []
for num in numbers:
    if num > 10 and num%2==0:
        new_list.append(num)
print(new_list)