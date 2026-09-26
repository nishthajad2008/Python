list1 = [1, 2, 3, 4, 5,6,7,8,9]
list2 = [3, 4, 5, 6, 7]
new_list = []
for num in list1:
    if num in list2:
        new_list.append(num)
print(new_list)