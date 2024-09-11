class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = inf
        sell = -inf
        max_profit = 0
        for p in prices:
            if buy == inf:
                buy = p
            elif p < buy:
                buy = p
                sell = -inf
            elif p > sell:
                sell = p
            if sell - buy > max_profit:
                max_profit = sell - buy
        return max_profit