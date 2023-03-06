def solve_puzzle(Board, Source, Destination):
    rows, cols = len(Board), len(Board[0])
    queue = [(Source, [Source])]
    visited = set()