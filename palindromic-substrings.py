def countSubstrings(self, s: str) -> int:
    palindrome_count = 0

    for i in range(len(s)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            palindrome_count += 1
            l -= 1
            r += 1
        
        # even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            palindrome_count += 1
            l -= 1
            r += 1
    return palindrome_count