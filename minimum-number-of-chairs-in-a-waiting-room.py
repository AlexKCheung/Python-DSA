def minimumChairs(self, s: str) -> int:
    counter = 0
    max_count = 0
    for i in range(len(s)):
        if s[i] == "E":
            counter += 1
            max_count = max(counter, max_count)
        else:
            counter -= 1
    return max_count