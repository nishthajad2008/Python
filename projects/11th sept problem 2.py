marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 64,
    "Emma": 38,
    "Frank": 72
}
cat_A = 0
cat_B = 0
cat_C = 0
cat_F = 0
for name, mark in marks.items():
    if mark >=80:
        cat_A +=1
    elif mark >=60:
        cat_B +=1
    elif mark >= 40:
        cat_C +=1
    else:
        cat_F +=1
print(f"A: {cat_A}")
print(f"B: {cat_B}")
print(f"C: {cat_C}")
print(f"F: {cat_F}")