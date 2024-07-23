def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key = lambda x: -x[1])
    max_units = 0
    for boxes, units in boxTypes:
        if truckSize > boxes:
            max_units += boxes * units
            truckSize -= boxes
        else:
            max_units += units * truckSize
            return max_units
    return max_units
        