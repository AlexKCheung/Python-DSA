def rob(self, nums: List[int]) -> int:
    
    def robber(nums):
        rob_one = 0
        rob_two = 0
        to_rob = 0
        for i in nums:
            to_rob = max(rob_two + i, rob_one)
            rob_two = rob_one
            rob_one = to_rob
        return to_rob

    return max(nums[0], robber(nums[1:]), robber(nums[:-1]))
