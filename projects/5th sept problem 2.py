number = int(input("Enter an integer: "))
if number <= 0:
    raise ValueError ("Integer to be positive only.")
else:
   total = 0
   for num in range(1,number+1):
      if num%2==0:
          total+=1
   print(f"Even number: {total}")