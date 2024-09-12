def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    count = 0
    for i in words:
        check = 0
        for c in i:
            if c not in allowed:
                check = 1
                break
        if check == 0:
            count += 1
    return count
            
            