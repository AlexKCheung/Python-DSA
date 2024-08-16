def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    max_ones = 0
    counter = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            counter = 0
        if nums[i] == 1:
            counter += 1
            max_ones = max(max_ones, counter)
    return max_ones