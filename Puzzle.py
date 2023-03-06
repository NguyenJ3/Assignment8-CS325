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