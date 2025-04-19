def removeElement(self, nums: List[int], val: int) -> int:
    i = 0
    k = 0
    end = len(nums) - 1

    while i < len(nums) and i <= end:
        if nums[i] == val:
            nums[i], nums[end] = nums[end], None
            end -= 1
        else:
            i += 1
            k += 1
    
    return k