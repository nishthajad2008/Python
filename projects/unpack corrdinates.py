points = [(1, 5), (2, 8), (3, 12), (4, 15)]
x_coords , y_coords = zip(*points)
print(f"x-coordinates:{x_coords}")
print(f"y-coordinates:{y_coords}")


# combining enumerate and zip
list_a = [100, 200, 300, 400]
list_b = [10, 20, 30]

for index, (a, b) in enumerate(zip(list_a, list_b)):
    print(f"Index {index} -> Item A: {a} | Item B: {b}")
    

