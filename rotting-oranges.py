def orangesRotting(self, grid: List[List[int]]) -> int:
    # bfs on rotten oranges 
    # iterate through length of queue, adding fresh oranges to end of queue

    queue = collections.deque()
    fresh_oranges = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                queue.append((row, col))
            if grid[row][col] == 1:
                fresh_oranges += 1
    
    time_elapsed = 0

    while queue and fresh_oranges > 0:
        for i in range(len(queue)):
            r, c = queue.popleft()
            for a, b in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                rr, cc = r + a, c + b
                if rr < 0 or cc < 0 or rr == len(grid) or cc == len(grid[0]):
                    continue
                if grid[rr][cc] == 0 or grid[rr][cc] == 2:
                    continue
                # change cell from fresh to rotten
                fresh_oranges -= 1
                grid[rr][cc] = 2
                queue.append((rr, cc))

        time_elapsed += 1
    
    return time_elapsed if fresh_oranges == 0 else -1