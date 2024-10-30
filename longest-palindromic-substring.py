def longestPalindrome(self, s: str) -> str:
    output = ""
    len_output = 0
    
    for i in range(len(s)):
        # check palindrome 
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len_output:
                output = s[l:r + 1]
                len_output = r - l + 1
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len_output:
                output = s[l:r + 1]
                len_output = r - l + 1
            l -= 1
            r += 1
    return output