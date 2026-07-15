languages = ['Spanish', 'English', 'Russian', 'Chinese']

index = 0

for language in languages:
    print(f'Index {index} and language {language}')
    index += 1

#an easier way to do that is by using the enumerate() function.
#1: enumerate(): keeps track of the index for an iterable and returns an enumerate object.

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages , 1): # the 1 here will make sure index starts from 1
    print(f'Index {index} and language {language}')
# output : Index 1 and language Spanish
#          Index 2 and language English
#          Index 3 and language Russian
#          Index 4 and language Chinese
# 2: zip() : combines lists into pairs of elements and returns an iterator of tuples.
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')
# n this example, zip() combines the two lists into pairs of elements and returns an iterator of tuples.
# The for loop then unpacks each tuple into name and id.
# Finally, for each print statement, we are printing each name and id from the ids and developers lists respectively.
# output. Name: Naomi
#         ID: 1
#         Name: Dario
#         ID: 2
#         Name: Jessica
#         ID: 3
#         Name: Tom
#         ID: 4