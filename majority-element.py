def majorityElement(self, nums: List[int]) -> int:
    # just use a count since we know it appears more than n/2 times 
    count = 0
    cur_num = nums[0]
    for i in range(len(nums)):
        if nums[i] == cur_num:
            count += 1
        else:
            count -= 1
            if count < 0:
                count = 1
                cur_num = nums[i]
    return cur_num