"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

def minMeetingRooms(self, intervals: List[Interval]) -> int:
    startTimes = sorted(i.start for i in intervals)
    endTimes = sorted(i.end for i in intervals)

    i, j = 0, 0
    active = 0
    output = 0

    while i < len(startTimes):
        if startTimes[i] < endTimes[j]:
            active += 1
            i += 1
        else:
            active -= 1
            j += 1
        output = max(output, active)
    return output 
