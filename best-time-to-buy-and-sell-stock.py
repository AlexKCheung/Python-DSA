def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    buy_price = prices[0]
    for i in prices:
        profit = max(profit, i - buy_price)
        buy_price = min(buy_price, i)
    return profit
