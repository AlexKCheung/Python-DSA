def finalPrices(self, prices: List[int]) -> List[int]:
    # O(n^2) runtime? 
    for i in range(len(prices)):
        for j in range(i+1, len(prices), 1):
            if prices[j] <= prices[i]:
                prices[i] = prices[i] - prices[j]
                break
    return prices
