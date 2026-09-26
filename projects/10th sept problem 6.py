numbers = [4, 7, 2, 9, 5, 12, 8]
summation = 0
for summ in numbers:
    summation +=summ
print(f"Sum: {summation}")
average = summation / len(numbers)
print(f"Average: {average:.2f}")
count = 0
for num in numbers:
    if num > average:
        count+=1
print(f"Above Average: {count}")
