# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicated OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuples = () ordered and unchangeable. Duplicates OK. FASTER


fruits = ["apple", "orange","banana","coconut"]

#exercise 1
print(fruits[0]) # first element of list
print(fruits[-1]) # last element of list
print(fruits[0:3]) # first 3 elements
print(fruits[::2]) # every second element beginning from 0
print(fruits[::-1]) # reverse of the list
print(len(fruits)) #number of elements in the list
print("apple" in fruits) # will ans as true or false and case of word matters
fruits[0] = "pineapple" # changes that element to the new element that is now apple will be pineapple
fruits.append("mango") #will add the element to the list
fruits.remove("mango") #will remove tha element from the list
fruits.insert(0, "dragonfruit") #will add it as per the given index
fruits.sort() #will sort it as per alphabetical order

print(fruits)

#exercise 2
for fruit in fruits:
    print(fruit)
