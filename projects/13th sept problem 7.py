set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3=set()
for num in set1:
    if num in set2:
        set3.add(num)
print(set3)