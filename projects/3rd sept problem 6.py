username = input("Enter your username: ")
password = input("Enter the password: ")
if username == "stark":
    if password == "jarvis123":
        print("Login Successful")
    else:
        print("Incorrect password")
else:
    print("User not found")