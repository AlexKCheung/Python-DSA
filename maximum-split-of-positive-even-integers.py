def maximumEvenSplit(self, finalSum: int) -> List[int]:
    if finalSum % 2 == 1:
        return []
    
    output = set()
    output_sum = 0
    i = 2

    while output_sum < finalSum:
        output.add(i)
        output_sum += i
        i += 2
    
    if output_sum == finalSum:
        return output
    
    for i in output:
        if output_sum - i == finalSum:
            output.remove(i)
            return output
