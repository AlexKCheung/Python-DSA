def majorityElement(self, nums: List[int]) -> int:
    # Boyer Moore majority vote algorithm
    candidate = None
    count = 0
    for i in range(len(nums)):
        if count == 0:
            candidate = nums[i]
            count = 1
        elif candidate == nums[i]:
            count += 1
        # candidate != nums[i]
        else: 
            count -= 1
    return candidate if count > 0 else None