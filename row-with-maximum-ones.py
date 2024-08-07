def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
    ones = 0
    row = 0
    for i in range(len(mat)):
        temp_counter = 0
        for j in mat[i]:
            if j == 1:
                temp_counter += 1
        if temp_counter > ones:
            ones = temp_counter
            row = i
    return [row, ones]

    # O(m x n) runtime
    # O(1) storage
