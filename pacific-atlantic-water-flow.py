def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    # keep track of cells that can be reached by what oceans
    pacific_set = set()
    atlantic_set = set()

    def dfs(r, c, ocean_set, prev_height):
        # already seen 
        if (r, c) in ocean_set:
            return
        # out of bounds
        if r < 0 or c < 0 or r == len(heights) or c == len(heights[0]):
            return
        # water can't flow to higher ground
        if heights[r][c] < prev_height:
            return 
        
        # add cell to mark as accessible by ocean
        ocean_set.add((r, c))

        # dfs on cell
        dfs(r + 1, c, ocean_set, heights[r][c])
        dfs(r - 1, c, ocean_set, heights[r][c])
        dfs(r, c + 1, ocean_set, heights[r][c])
        dfs(r, c - 1, ocean_set, heights[r][c])
        return 
    
    for row in range(len(heights)):
        dfs(row, 0, pacific_set, heights[row][0])
        dfs(row, len(heights[0]) - 1, atlantic_set, heights[row][-1])
    
    for col in range(len(heights[0])):
        dfs(0, col, pacific_set, heights[0][col])
        dfs(len(heights) - 1, col, atlantic_set, heights[-1][col])

    # return list(pacific_set & atlantic_set)
    output = []
    for row in range(len(heights)):
        for col in range(len(heights[0])):
            if (row, col) in pacific_set and (row, col) in atlantic_set:
                output.append((row, col))
    return output