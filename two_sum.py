def twoSum(self, nums: List[int], target: int) -> List[int]:
    # have dictionary where key, value = nums value, index
    values = {}
    for i in range(len(nums)): 
        if target - nums[i] in values: 
            return [i, values[target - nums[i]]]
        else: 
            values[nums[i]] = i
    
    return [0,1]