import time
time.sleep(3) # after 3 seconds it will display times up
print("TIME'S UP!!")

#1
my_time = int(input("Enter the time in seconds: "))
for x in reversed(range(0, my_time)):# this will end at 0
    print(x)
    time.sleep(1)

#2
my_time = int(input("Enter the time in seconds: "))
for x in range(my_time,0,-1):
    print(x)
    time.sleep(1)
print("TIME'S UP!!")

#3
my_time = int(input("Enter the time in seconds: "))
for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x/60)
    hours = int(x/3600)
    print(f"{hours}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP!!")
#run all indivitually or there will be error
