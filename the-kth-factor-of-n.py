def kthFactor(self, n: int, k: int) -> int:
    output = -1
    mod_num = n
    # factor until n/2 from previouis knowledge
    for i in range(1, n//2 + 1):
        if mod_num % i == 0:
            output = i
            k -= 1
        if k == 0:
            return output
    if k == 1:
        return n
    return -1
        
