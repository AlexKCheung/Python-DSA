def exist(self, board: List[List[str]], word: str) -> bool:
    # m = row, n = col, from m x n board
    m = len(board)
    n = len(board[0])
    seen = set()

    def dfs(i, j, index):
        if index == len(word):
            return True
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
            return False
        if (i, j) in seen:
            return False
        if board[i][j] != word[index]:
            return False
        seen.add((i, j))
        index += 1
        next_dfs = dfs(i+1, j, index) or dfs(i-1, j, index) or dfs(i, j+1, index) or dfs(i, j-1, index)
        seen.remove((i, j))
        return next_dfs
    
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False
