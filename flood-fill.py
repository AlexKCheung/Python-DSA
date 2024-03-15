def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    row = len(image)
    col = len(image[0])
    # changable color
    original_color = image[sr][sc]
    
    def dfs(i, j): 
        # >= because index is zero based
        if i < 0 or i >= row or j < 0 or j >= col: 
            return
        # if already changed square or not a changable square
        if image[i][j] == color or image[i][j] != original_color:
            return
        # change current square 
        image[i][j] = color 
        # call dfs on 4 directions
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    dfs(sr, sc)
    return image