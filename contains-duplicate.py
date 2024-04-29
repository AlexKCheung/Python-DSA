def containsDuplicate(self, nums: List[int]) -> bool:
    # can also use hash map dictionary for linear time
    return len(nums) != len(set(nums))