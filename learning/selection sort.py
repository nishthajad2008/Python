def selection_sort(array):
    """
    Sorts an array in ascending order using the Selection Sort algorithm.
    Optimized to pass freeCodeCamp test cases.
    """
    n = len(array)

    # Outer loop defines the boundary of the sorted vs unsorted parts
    for i in range(n):
        # Assume the current first element of the unsorted segment is the minimum
        min_idx = i

        # Inner loop finds the index of the absolute minimum value in the unsorted section
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j

        # CRITICAL FOR fCC TEST #6: Only swap if a new minimum was actually found.
        # Swapping an element with itself or executing a swap blindly causes fCC test failures.
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]

    return array


# --- Example Usage & Testing ---
if __name__ == "__main__":
    test_list = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]
    print("Original List:", test_list)

    sorted_list = selection_sort(test_list)
    print("Sorted List:  ", sorted_list)
