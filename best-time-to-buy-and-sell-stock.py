def maxProfit(self, prices: List[int]) -> int:
    min_day = prices[0]
    max_profit = 0

    for i in range(len(prices)): 
        if prices[i] < min_day:
            min_day = prices[i]
        max_profit = max(max_profit, prices[i] - min_day)

    return max_profit