def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    highest_candies = 0
    for i in range(len(candies)):
        if candies[i] > highest_candies:
            highest_candies = candies[i]
    # can do a new array or just replace for O(1) space
    for i in range(len(candies)):
        if candies[i] + extraCandies >= highest_candies:
            candies[i] = True
        else:
            candies[i] = False
    return candies