def rob(self, nums: List[int]) -> int:
    prev_two = 0
    prev_one = 0
    cur = 0
    # [prev_two, prev_one, i, i + 1, ...]
    for i in nums:
        cur = max(i + prev_two, prev_one)
        prev_two = prev_one
        prev_one = cur
    return cur
    