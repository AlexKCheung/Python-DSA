def climbStairs(self, n: int) -> int:
    cur = 1
    prev = 1

    for i in range(n - 1): 
        temp = cur
        cur = cur + prev
        prev = temp

    return cur