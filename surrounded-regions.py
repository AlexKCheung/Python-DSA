def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # for each edge piece that is 'O', do dfs and add places to seen set
    # then each 'O' that is not in the seen set get changed to 'X'

    connected_edge_pieces = set()

    def outer_dfs(row, col):
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]):
            return 
        if board[row][col] == "X":
            return
        # cell is "O"
        # already seen
        if (row, col) in connected_edge_pieces:
            return
        connected_edge_pieces.add((row, col))
        outer_dfs(row + 1, col)
        outer_dfs(row - 1, col)
        outer_dfs(row, col + 1)
        outer_dfs(row, col - 1)
        return
    
    def inner_dfs(row, col):
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]):
            return
        if board[row][col] == "X":
            return
        if (row, col) in connected_edge_pieces:
            return
        # cell is "O" and not connected to edges
        board[row][col] = "X"
        inner_dfs(row + 1, col)
        inner_dfs(row - 1, col)
        inner_dfs(row, col + 1)
        inner_dfs(row, col - 1)
        return

    for i in range(len(board)):
        if board[i][0] == "O":
            outer_dfs(i, 0)
        if board[i][len(board[0]) - 1] == "O":
            outer_dfs(i, len(board[0]) - 1)
    
    for j in range(len(board[0])):
        if board[0][j] == "O":
            outer_dfs(0, j)
        if board[len(board) - 1][j] == "O":
            outer_dfs(len(board) - 1, j)
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "O":
                inner_dfs(r, c)
                