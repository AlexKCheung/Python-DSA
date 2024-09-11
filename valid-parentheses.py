# def isValid(self, s: str) -> bool:
#     parentheses = {'(': ')', '{': '}', '[': ']'}
#     sentence = []
#     for i in range(len(s)): 
#         if s[i] in parentheses: 
#             sentence.append(s[i])
#         # we're given only ()[]{} in s
#         else: 
#             if len(sentence) == 0: 
#                 return False
#             elif parentheses[sentence.pop()] == s[i]:
#                 continue
#             else: 
#                 return False
#     return len(sentence) == 0


def isValid(self, s: str) -> bool:
    queue = []
    brackets = {"(": ")", "[": "]", "{": "}"}

    for i in s:
        if i in brackets.keys():
            queue.append(i)
        else:
            if len(queue) > 0:
                top = queue.pop()
                if brackets[top] != i:
                    return False
            else:
                return False
    return len(queue) == 0