def column_sums(matrix):
    n = len(matrix)
    result = []

    for col in range(len(matrix[0])):
        col_sum = 0
        for row in range(len(matrix)):
            col_sum += matrix[row][col]
        result.append(col_sum)
    return result
if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(column_sums(matrix))
