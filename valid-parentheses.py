def isValid(self, s: str) -> bool:
    parentheses = {'(': ')', '{': '}', '[': ']'}
    sentence = []
    for i in range(len(s)): 
        if s[i] in parentheses: 
            sentence.append(s[i])
        # we're given only ()[]{} in s
        else: 
            if len(sentence) == 0: 
                return False
            elif parentheses[sentence.pop()] == s[i]:
                continue
            else: 
                return False
    return len(sentence) == 0