def solve_puzzle(Board, Source, Destination):
    rows, cols = len(Board), len(Board[0])
    queue = [(Source, [Source])]
    visited = set()
    while queue:
        # get the current cell and its path from the queue
        (i, j), path = queue.pop(0)
        # check if the current cell is the destination, and return the path if it is
        if (i, j) == Destination:
            return path
        for ni, nj in ((i-1, j), (i, j+1), (i+1, j), (i, j-1)):
            if 0 <= ni < rows and 0 <= nj < cols and Board[ni][nj] == '-' and (ni, nj) not in visited:
                # mark cell as visited and add it to the queue with its path
                visited.add((ni, nj))
                queue.append(((ni, nj), path + [(ni, nj)]))
    # if no path to destination is found, return None
    return None

#3a) In order to solve for the problem is through the Breadth-First Search (BFS) through visiting each cell we can check for an empty one then add it to the queue

#3c) Time complexity is O(mn)