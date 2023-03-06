def Prims(G):
    n = len(G)
    visited = [False] * n
    key = [float('inf')] * n
    parent = [None] * n
    key[0] = 0