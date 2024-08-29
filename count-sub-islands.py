def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    # dfs on non island 2 if island 2 has land but not island 1
    # then count islands on 2 by dfs

    ROW = len(grid1)
    COL = len(grid1[0])

    def dfs(i, j):
        if i < 0 or i == ROW or j < 0 or j == COL or grid2[i][j] == 0:
            return
        # else land in bounds
        grid2[i][j] = 0
        for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
            dfs(i + x, j + y)
    
    for i in range(ROW):
        for j in range(COL):
            if grid2[i][j] == 1 and grid1[i][j] == 0:
                dfs(i, j)

    island_count = 0
    for i in range(ROW):
        for j in range(COL):
            if grid2[i][j] == 1:
                dfs(i, j)
                island_count += 1
    return island_count
