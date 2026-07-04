#nested loop = A loop within another loop (outer, inner)
#              outer loop:
#                  inner loop:
for x in range( 1, 10):
    print(x) #this will give numbers on different lines
for x in range(1 , 10):
    print(x, end=" ") #all the number on same line
for x in range(3):
    for y in range(1,10):
        print(y, end=" ")
    print()
# exercise
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol: ")
for x in range(row):
    for y in range(col):
      print(symbol, end="")
    print()