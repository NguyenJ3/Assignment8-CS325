def Prims(G):
    n = len(G)
    visited = [False] * n
    key = [float('inf')] * n
    parent = [None] * n
    key[0] = 0
    for i in range(n):
        u = min((key[j], j) for j in range(n) if not visited[j])[1]   # select the vertex with minimum key value that is not visited
        visited[u] = True           # mark the selected vertex as visited