def square_even(num):
    result = []
    for i in num:
        if i % 2 == 0:
            result.append(i**2)
    print(result)
(square_even([1,2,3,4,5,6,7,8,9,10]))
