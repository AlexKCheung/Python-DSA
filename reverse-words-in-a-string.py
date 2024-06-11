def reverseWords(self, s: str) -> str:
    words = []
    temp = ""
    for i in range(len(s)):
        if s[i] != " ":
            temp += s[i]
        elif temp != "":
            words.append(temp)
            temp = ""
    if temp != "":
        words.append(temp)
    return " ".join(words[::-1])
