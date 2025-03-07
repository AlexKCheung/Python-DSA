def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key = lambda x:x[0])
    output = [intervals[0]]

    for i in intervals:
        if i[0] <= output[-1][1]:
            output[-1][1] = max(output[-1][1], i[1])
        else:
            output.append(i)
    return output
