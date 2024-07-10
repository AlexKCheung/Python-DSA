def numberOfPairs(self, nums: List[int]) -> List[int]:
    unique_numbers = []
    operations = 0
    for i in nums:
        if i in unique_numbers:
            unique_numbers.remove(i)
            operations += 1
        else:
            unique_numbers.append(i)
    return [operations, len(unique_numbers)]
        