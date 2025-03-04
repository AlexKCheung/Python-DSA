def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
    less_than = []
    greater_than = []
    # count number of equals 
    equal_to = 0
    for i in nums:
        if i < pivot:
            less_than.append(i)
        elif i > pivot: 
            greater_than.append(i)
        else:
            equal_to += 1
    return less_than + [pivot] * equal_to + greater_than
