def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    for i in nums:
        if i not in count:
            count[i] = 0
        count[i] += 1
    
    frequency = [[] for i in range(len(count) + 1)]
    for n, c in count.items():
        frequency[c].append(n)
    
    output = []
    for i in range(len(frequency) - 1, 0, -1):
        for j in frequency[i]:
            output.append(j)
            if len(output) == k:
                return output
