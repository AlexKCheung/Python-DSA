def longestPalindrome(self, s: str) -> int:
    letters = {}
    for i in range(len(s)):
        if s[i] in letters:
            letters[s[i]] += 1
        else:
            letters[s[i]] = 1
    
    has_odd = 0
    length = 0

    for i in letters:
        if letters[i] % 2 == 0:
            length += letters[i]
        elif letters[i] > 1:
            length += letters[i] - 1
            has_odd += 1
        else:
            has_odd += 1
    if has_odd > 0:
        length += 1
    return length
