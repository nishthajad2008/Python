# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.
for x in range(1,11):
    print(x)
for x in reversed(range(1,11)): # reversing
    print(x)
for x in range(1,11,2): #a gap of 2 i.e 1,3,5,7,9
    print(x)
credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)
for x in range(1,21): # to skip a number lets say 13 and 19
    if x == 13 or x == 19:
        continue
    else:
        print(x)
for x in range(1,21): # to stop when reached at 12 i.e only till 1 to 12
    if x == 13:
        break
    else:
        print(x)