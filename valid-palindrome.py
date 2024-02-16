def isPalindrome(self, s: str) -> bool:
    # helper functions .isalnum() .lower()
    # stack: until halfway, then pop stack until end 
    # iterate until half while checking if s[i] == -s[i]
    # can one pass this way

    new_string = []
    for i in range(len(s)): 
        if s[i].isalnum(): 
            new_string.append(s[i].lower())
    for i in range(len(new_string) // 2): 
        if new_string[i] != new_string[-(i + 1)]: 
            return False
    return True
    
