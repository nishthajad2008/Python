#logical operators = evaluate multiple conditions (or, and, not)
#               or = at least one condition must be Truw
#              and = both conditions must be True
#              not = inverts the condition ( not False, not True)

# or statement
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is scheduled")

#and statement
temp = 25
is_sunny = True
if temp >= 28 and is_sunny:
    print("Is is HOT outside")
    print("It is sunny outside")
elif temp <= 0 and is_sunny:
    print("Its cold outside")
    print("Is is sunny outside")
elif 28 >temp>0 and is_sunny:
    print("It is sunny outside")
else:
    print("It is not sunny outside")

# not statement
temp = 25
is_raining = False
if temp > 35 and not is_raining:
    print("It is hot outside")
elif temp <= 0 and not is_raining:
    print("It is cold outside")
elif 35 > temp>0 and is_raining:
    print("It is raining outside")
elif temp > 35 and  is_raining:
    print("It is hot and raining outside")
elif temp <= 0 and is_raining:
    print("It is cold and raining outside")
else:
    print("It is a perfect day")




