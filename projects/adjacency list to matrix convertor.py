def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    matrix = [[0]*n for _ in range(n)]
    for node,neighbours in adj_list.items():
        for neigh in neighbours:
            matrix[node][neigh]=1
    for row in matrix:
        print(row)
    return matrix