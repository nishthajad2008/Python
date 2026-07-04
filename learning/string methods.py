name = input("Enter your full name: ")

result = len(name)  # number of letters, includes space
print(result)
result = name.find("N")  # position of it but if multiple it will give for the first one
print(result)
result = name.rfind("h")  # reverse, find the last occurrence
print(result)
name = name.capitalize()  # capitalizes the first letter
name = name.upper()  # capitalizes the whole thing
name = name.lower()  # lower case of the whole thing
result = name.isdigit()  # if only numbers then true or else false
result = name.isalpha()  # if only alphabets then true or else false
print(name)
print(result)
phone_number = input("Enter your phone number: ")
result = phone_number.count("8")
result = phone_number.replace("8", "3")
print(result)
print(help(str))  # help give us the info about the function or the attribute used

#exercise
username = input("Enter your username: ")
if  len(username) > 12:
    print("username is too long. must ne less than 12 characters")
elif not username.find(" ") == -1:
    print("username can't contain space")
elif not username.isalpha():
    print("username can't contain number")
else:
    print(f"{username} is a valid username")