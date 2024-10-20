def lengthOfLongestSubstring(self, s: str) -> int:
    longest_length = 0
    # two pointers
    front = 0
    back = 0
    # o(n) space, stack 
    current_substring = set()

    while front < len(s):
        if s[front] not in current_substring:
            current_substring.add(s[front])
            longest_length = max(longest_length, front - back + 1)
            # front += 1
        else: # s[front] in current_substring
            while s[back] != s[front]:
                current_substring.remove(s[back])
                back += 1
            back += 1
        front += 1
    
    return longest_length 
