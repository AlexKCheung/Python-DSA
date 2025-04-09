def characterReplacement(self, s: str, k: int) -> int:
    l, r = 0, 0
    longest = 0
    counts = dict()

    while r < len(s):
        if s[r] not in counts:
            counts[s[r]] = 1
        else:
            counts[s[r]] += 1
        
        cur_window = r - l + 1
        if cur_window - max(counts.values()) <= k:
            longest = max(longest, cur_window)
        else:
            counts[s[l]] -= 1
            l += 1
        r += 1
    return longest