def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    leftovers = []
    full = 0
    for i in range(len(capacity)):
        remaining = capacity[i] - rocks[i]
        if remaining == 0:
            full += 1
        else:
            leftovers.append(remaining)
    leftovers.sort()
    for i in range(len(leftovers)):
        if leftovers[i] - additionalRocks <= 0:
            additionalRocks -= leftovers[i]
            full += 1
        else:
            break
    return full
        
        
