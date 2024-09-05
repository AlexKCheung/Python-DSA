def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
    
    # len(rolls) + n = total_length
    # mean = (rolls + X) / (len(rolls) + n)
    # mean * (len(rolls) + n) - rolls = X
    # check if X is divisible by n and the remainder can be split evenly

    x = mean * (len(rolls) + n) - sum(rolls)
    # check if possible
    if x / n > 6 or x / n < 1:
        return []
    if x % n == 0:
        # / gives doubles instead of ints
        return [x//n] * n

    output = [x//n] * n
    for i in range(x % n):
        output[i] += 1
    return output
    