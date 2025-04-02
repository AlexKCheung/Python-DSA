def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # two pointers, if greater move right, if lesser move left

    l, r = 0, len(numbers) - 1
    combined = numbers[l] + numbers[r]
    while combined != target:
        if combined > target:
            r -= 1
        elif combined < target:
            l += 1
        combined = numbers[l] + numbers[r]
    
    return [l + 1, r + 1]