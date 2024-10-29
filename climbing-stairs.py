def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    prev_two = 0
    prev_one = 1
    output = 0
    for i in range(n):
        output = prev_one + prev_two
        prev_two = prev_one
        prev_one = output
    return output
    