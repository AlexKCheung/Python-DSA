def isPossibleToSplit(self, nums: List[int]) -> bool:
    # if array is sorted then we only need to check if a number's prev and next is the same as curr
    # since not stated in problem, can either sort array first or have a dictionary counter
    counter = {}
    for i in range(len(nums)): 
        if nums[i] in counter: 
            counter[nums[i]] += 1
        else: 
            counter[nums[i]] = 1
    for i in counter: 
        if counter[i] > 2: 
            return False
    return True