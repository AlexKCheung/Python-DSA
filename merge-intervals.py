def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key = lambda x: x[0])
    output = []
    output.append(intervals[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] <= output[-1][1]:
            bigger_end = max(output[-1][1], intervals[i][1])
            output[-1] = [output[-1][0], bigger_end]
        else:
            output.append(intervals[i])
    return output

