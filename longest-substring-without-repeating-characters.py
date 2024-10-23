def lengthOfLongestSubstring(self, s: str) -> int:
    longest_length = 0
    r = 0
    l = 0
    cur_str = set()

    while r < len(s):
        if s[r] in cur_str:
            while s[r] in cur_str:
                cur_str.remove(s[l])
                l += 1
        cur_str.add(s[r])
        r += 1
        longest_length = max(longest_length, r - l)
    
    return longest_length