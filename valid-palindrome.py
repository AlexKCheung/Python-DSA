def isPalindrome(self, s: str) -> bool:
    # helper functions .isalnum() .lower()
    # another method stack: until halfway, then pop stack until end

    # new_string = []
    # for i in range(len(s)): 
    #     if s[i].isalnum(): 
    #         new_string.append(s[i].lower())
    # for i in range(len(new_string) // 2): 
    #     if new_string[i] != new_string[-(i + 1)]: 
    #         return False
    # return True

    # faster two pointer 
    l, r = 0, len(s) - 1
    while l < r: 
        while l < r and not s[l].isalnum(): 
            l += 1
        while l < r and not s[r].isalnum(): 
            r -= 1
        if s[l].lower() != s[r].lower(): 
            return False
        l += 1
        r -= 1
    return True
