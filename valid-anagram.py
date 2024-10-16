def isAnagram(self, s: str, t: str) -> bool:
    alphabet = [0] * 26
    for i in s:
        alphabet[ord(i) - ord('a')] += 1
    for i in t:
        alphabet[ord(i) - ord('a')] -= 1
        
    for i in alphabet:
        if i != 0:
            return False
    return True

# def isAnagram(self, s: str, t: str) -> bool:
#     counter = {}
#     for i in range(len(s)): 
#         if s[i] in counter: 
#             counter[s[i]] += 1
#         else: 
#             counter[s[i]] = 1

#     for i in range(len(t)): 
#         if not t[i] in counter: 
#             return False
#         else: 
#             counter[t[i]] -= 1
    
#     for i in counter: 
#         if counter[i] != 0: 
#             return False
#     return True

#     # can also do return sorted(s) == sorted(t)