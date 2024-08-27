def orangesRotting(self, grid: List[List[int]]) -> int:
    fresh_oranges = 0
    rotten_q = collections.deque() 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                fresh_oranges += 1
            if grid[i][j] == 2:
                rotten_q.append((i, j))
    if fresh_oranges == 0:
        return 0
    if not rotten_q:
        return -1
    
    minutes = 0
    while rotten_q and fresh_oranges > 0:
        minutes += 1

        for i in range(len(rotten_q)):
            x, y = rotten_q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                xx, yy = x + dx, y + dy
                if xx < 0 or xx == len(grid) or yy < 0 or yy == len(grid[0]):
                    continue
                if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                    continue
                grid[xx][yy] = 2
                rotten_q.append((xx, yy))
                fresh_oranges -= 1

    if fresh_oranges != 0:
        return -1
    return minutes


