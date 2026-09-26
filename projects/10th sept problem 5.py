numbers = [12, 45, 7, 23, 45, 19, 31]
new_list = []
for num in numbers:
    if num not in new_list:
        new_list.append(num)
largest = new_list[0]
for numm in new_list:
    if numm > largest:
        largest = numm
new_list.remove(largest)
second_largest = new_list[0]
for second in new_list:
    if second > second_largest:
        second_largest = second
print(f"Second Largest: {second_largest}")