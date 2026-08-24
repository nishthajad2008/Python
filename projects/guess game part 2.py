secret_num = 9
number = int(input("Enter the secret number: "))
while number != secret_num:
    print("WRONG! Try Again")
    number = int(input("Enter the secret number: "))
print("Access Granted!")