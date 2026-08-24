def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.append(current)

            # Look through all potential neighbors for the current node
            # Iterating in reverse ensures smaller node indices are processed first
            for neighbor in range(len(graph[current]) - 1, -1, -1):
                if graph[current][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

    return visited