def solve_puzzle(Board, Source, Destination):
    rows, cols = len(Board), len(Board[0])
    queue = [(Source, [Source])]
    # set to keep track of visited cells
    visited = set()
    # dictionary to map differences between adjacent cells to directions
    dir_map = {(-1, 0): 'U', (0, 1): 'R', (1, 0): 'D', (0, -1): 'L'}
    # initialize previous cell as the source
    prev = Source
    while queue:
        # get the current cell and its path from the queue
        (i, j), path = queue.pop(0)
        if (i, j) == Destination:
            # calculate the directions from the path
            directions = ''.join([dir_map[(i-pi, j-pj)] for (pi, pj), (i, j) in zip(path, path[1:])])
            return path, directions
        # check each adjacent cell and add it to the queue if it is valid and unvisited
        for ni, nj in ((i-1, j), (i, j+1), (i+1, j), (i, j-1)):
            if 0 <= ni < rows and 0 <= nj < cols and Board[ni][nj] == '-' and (ni, nj) not in visited:
                # mark cell as visited and add it to the queue with its path
                visited.add((ni, nj))
                queue.append(((ni, nj), path + [(ni, nj)]))
        # update previous cell as the current cell
        prev = (i, j)
    # if no path to destination is found, return None for both path and directions
    return None, None

#3a) In order to solve for the problem is through the Breadth-First Search (BFS) through visiting each cell we can check for an empty one then add it to the queue

#3c) Time complexity is O(mn)