score = float(input("Enter your score: "))
if score < 0 or score > 100:
    raise ValueError("Score needs to be between 0 and 100")
if score >= 90:
    print(f"Score: {score}")
    print(f"Grade: A")
elif score >=80:
    print(f"Score: {score}")
    print(f"Grade: B")
elif score >=70:
    print(f"Score: {score}")
    print(f"Grade: C")
elif score >=60:
    print(f"Score: {score}")
    print(f"Grade: D")
else:
    print(f"Score: {score}")
    print(f"Grade: F")

for row in range(1, 5):
    for column in range(row):
        print("*", end="")
    print()