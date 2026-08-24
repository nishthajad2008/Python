def square_root_bisection(number, tolerance=0.01, max_iter=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    low = 0
    high = max(1, number)
    root = None  # Track if a valid root is found

    for _ in range(max_iter):
        mid = (low + high) / 2
        # Use interval width for precision on small numbers
        if (high - low) <= tolerance:
            root = mid
            break
        if mid ** 2 < number:
            low = mid
        else:
            high = mid

    if root is None:
        print(f"Failed to converge within {max_iter} iterations")
        return None

    print(f"The square root of {number} is approximately {root}")
    return root
