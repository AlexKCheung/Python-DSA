def numIslands(self, grid: List[List[str]]) -> int:
    # bfs each island to mark as seen 
    islands = 0
    # add edges of the grid with a 0 water to handle out of bounds in bfs
    for row in grid:
        row.insert(0, "0")
        row.append("0")

    grid.insert(0, ["0"] * len(grid[0]))
    grid.append(["0"] * len(grid[0]))

    def dfs(grid, row_num, col_num):
        if grid[row_num][col_num] == "1":
            grid[row_num][col_num] = "-1"
            dfs(grid, row_num + 1, col_num)
            dfs(grid, row_num - 1, col_num)
            dfs(grid, row_num, col_num + 1)
            dfs(grid, row_num, col_num - 1)


    # ignore first and last as we know they're water and out of bounds
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] == "1":
                islands += 1
                dfs(grid, row, col)
    
    return islands
    