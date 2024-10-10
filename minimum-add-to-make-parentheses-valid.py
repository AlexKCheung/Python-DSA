def minAddToMakeValid(self, s: str) -> int:
    open = 0
    close = 0
    for i in s:
        if i == "(":
            open += 1
        elif i == ")" and open > 0:
            open -= 1
        else:
            close += 1
    return open + close