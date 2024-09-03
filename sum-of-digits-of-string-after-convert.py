def getLucky(self, s: str, k: int) -> int:
    output = ""
    for i in s:
        output += str(ord(i) - ord('a') + 1)
    
    while k > 0:
        output = str(output)
        temp = 0
        for i in output:
            temp += int(i)
        output = temp
        k -= 1

    return output