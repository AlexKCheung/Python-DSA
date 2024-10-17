def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counts = {}
    for i in nums:
        counts[i] = counts.get(i, 0) + 1
    
    frequency = [[] for i in range(len(nums) + 1)]
    for num, count in counts.items():
        frequency[count].append(num)
    
    output = []
    for i in range(len(frequency) - 1, 0, -1):
        for j in frequency[i]:
            output.append(j)
            if len(output) == k:
                return output