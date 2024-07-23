def firstUniqChar(self, s: str) -> int:
    seen = {}
    for i in s:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1
    for i in range(len(s)):
        if seen[s[i]] == 1:
            return i
    return -1
    