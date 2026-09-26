numbers = [2, 5, 2, 8, 5, 2, 9, 5]
ex_dict = {}
count = 1
for num in numbers:
    if num in ex_dict:
        ex_dict[num]+=1
    else:
        ex_dict[num] = 1
print(ex_dict)