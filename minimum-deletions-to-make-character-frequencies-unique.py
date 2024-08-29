def minDeletions(self, s: str) -> int:
    frequencies = [0] * 26
    for i in s:
        frequencies[ord(i) - ord('a')] += 1
    frequencies.sort(reverse=True)

    output = 0
    seen_freq = set()
    for i in range(len(frequencies)):
        if frequencies[i] == 0:
            break
        while frequencies[i] > 0 and frequencies[i] in seen_freq:
            output += 1
            frequencies[i] -= 1
        seen_freq.add(frequencies[i])
        
    return output
