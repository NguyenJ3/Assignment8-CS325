def Prims(G):
    n = len(G)
    visited = [False] * n
    key = [float('inf')] * n
    parent = [None] * n
    key[0] = 0
    for i in range(n):
        u = min((key[j], j) for j in range(n) if not visited[j])[1]   # select the vertex with minimum key value that is not visited
        visited[u] = True           # mark the selected vertex as visited
        for v in range(n):
            # update the key value and parent of adjacent vertices if they are not visited and their weight is smaller than the current key value
            if G[u][v] != 0 and not visited[v] and G[u][v] < key[v]:
                key[v] = G[u][v]
                parent[v] = u
      # create a list of tuples representing the edges of the MST
    mst = [(parent[i], i, G[i][parent[i]]) for i in range(1, n)]
    return mst

#2b) Kruskal's uses a greedy algorithm approach while Prim's algorithm uses priority queue 