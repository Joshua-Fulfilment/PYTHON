def findCenter(edges):
    n = len(edges) + 1
    
    adj_list = [[] for _ in range(n + 1)]

    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    for node in range(1, n + 1):
        if len(adj_list[node]) == n - 1:
            return node

    return -1  # If no center is found

# Example usage:
edges = [[1, 2], [2, 3], [4, 2]]
center = findCenter(edges)
print(center)

