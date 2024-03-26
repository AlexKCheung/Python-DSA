def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    counter = {}
    for i in range(len(ransomNote)):
        if ransomNote[i] in counter:
            counter[ransomNote[i]] += 1
        else:
            counter[ransomNote[i]] = 1

    for i in range(len(magazine)):
        if magazine[i] not in counter:
            continue
        counter[magazine[i]] -= 1
        
    for i in counter:
        if counter[i] > 0:
            return False
    return True