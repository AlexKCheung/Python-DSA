import math

def smallestDivisor(self, nums: List[int], threshold: int) -> int:

    def get_sum(divisor):
        cur_sum = 0
        for i in nums:
            cur_sum += int(math.ceil(i / divisor))
        if cur_sum <= threshold:
            return True
        return False
    
    # binary search
    l = 1
    r = max(nums)
    while l < r:
        mid = (l + r) // 2
        if not get_sum(mid):
            l = mid + 1
        else:
            r = mid
    return l