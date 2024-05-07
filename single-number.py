def singleNumber(self, nums: List[int]) -> int:
    # previously put count in dictionary and count occurences
    xor_number = 0
    for i in nums:
        xor_number ^= i
    return xor_number