#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step] step is basically skipping character

credit_number = "1234-5678-9012-3456"
print(credit_number[0]) #first character
print(credit_number[0:4]) or print(credit_number[:4])#the characters from place 0 to 3, doesnt include 4
print(credit_number[5:]) # characters from 5 to end
print(credit_number[-1]) #end character. -2 will be the second last character and so on
print(credit_number[::2]) #will print every second character in the string
print(credit_number[-4:]) # for only last four digits
print(credit_number[::-1]) # to reverse the whole thing
