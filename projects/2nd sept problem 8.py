age = int(input("Enter your age: "))
email_status = (input("Email verification status (True or False):"))
verify = age >=18 and email_status == "True"
print(f"Can login? {verify}")

