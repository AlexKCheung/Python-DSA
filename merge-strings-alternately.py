def mergeAlternately(self, word1: str, word2: str) -> str:
    output = ""
    first = 0
    second = 0
    while first < len(word1) and second < len(word2):
        output += word1[first]
        output += word2[second]
        first += 1
        second += 1
    
    if first == len(word1):
        output += word2[second:]
    else:
        output += word1[first:]
    return output