#You are given a string .
#Your task is to find out if the string  contains:
# alphanumeric characters
# alphabetical characters
# digits
# lowercase
# uppercase characters.

if __name__ == '__main__':
    s = input("String: ")
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
# this is to learn that instead of multiple if statements, use this method if any task similar to this

