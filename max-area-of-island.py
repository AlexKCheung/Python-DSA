def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    max_area = 0

    def dfs(row, col):
        # out of bounds
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]):
            return 0
        if grid[row][col] == 0:
            return 0

        # cell is 1, set to 0 to not visit again
        grid[row][col] = 0

        return (
            1 +
            dfs(row + 1, col) + 
            dfs(row - 1, col) + 
            dfs(row, col + 1) + 
            dfs(row, col - 1)
        )
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                cur_area = dfs(r, c)
                max_area = max(max_area, cur_area)
    
    return max_area