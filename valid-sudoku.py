def isValidSudoku(self, board: List[List[str]]) -> bool:
    # iterate entire board
    for r in range(len(board)):
        for c in range(len(board)):
            # validate filled cells only
            if board[r][c] != ".":
                for i in range(8):
                    # row
                    if board[r][c] == board[r][i] and i != c:
                        return False
                    # col
                    if board[r][c] == board[i][c] and i != r:
                        return False
    
    # 3 x 3 sub-boxes, multiply by the r/c + 1-3
    for r in range(3):
        for c in range(3):
            sub_box = set()
            # go through the 9 cells in a sub-box
            for i in range(3):
                cur_r = r * 3 + i
                for j in range(3):
                    cur_c = c * 3 + j
                    if board[cur_r][cur_c] == ".":
                        continue
                    if board[cur_r][cur_c] in sub_box:
                        return False
                    else:
                        sub_box.add(board[cur_r][cur_c])

    return True        

