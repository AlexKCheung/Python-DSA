def longestConsecutive(self, nums: List[int]) -> int:
    nums_set = set(nums)
    longest = 0
    for i in nums:
        # find the starts of each sequence
        if (i - 1) not in nums_set:
            cur_len = 1
            while (i + cur_len) in nums_set:
                cur_len += 1
            longest = max(longest, cur_len)
    return longest