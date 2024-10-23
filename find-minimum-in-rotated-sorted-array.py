def findMin(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
        
    l = 0
    r = len(nums) - 1
    while True:
        m = (l + r) // 2
        if nums[m] < nums[m - 1]:
            return nums[m]
        if nums[m] < nums[-1]:
            r = m - 1
        else:
            l = m + 1
        