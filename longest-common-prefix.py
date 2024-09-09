def longestCommonPrefix(self, strs: List[str]) -> str:
    strs.sort()
    first = strs[0]
    last = strs[-1]
    output = ""
    for i in range(len(first)):
        if first[i] == last[i]:
            output += first[i]
        else:
            break
    return output
